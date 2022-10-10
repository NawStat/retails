import pymongo
import csv
import pandas as pd
import sys
import os


class mongo_data:

    def __init__(self, host):
        self.host = host

    def _connect_to_mongodb(self, database, port=27017):
        """
        connect to the mongodb
        :param database: database name
        :return:
        """
        try:
            print("Connecting to ", database)
            myclient = pymongo.MongoClient("mongodb://" + self.host + ":" + str(port)+"/")
            # create DB
            return myclient[database]
        except Exception as e:
            print('Error while connecting to mongo ', database)
            print(e)

    def inject_data_to_mongodb(self, path_file, sheet, database, port=27017 ):
        """
        Inject xsl file into mongoDB
        :param path_file:
        :param sheet:
        :param database:
        :return:  None
        """
        try:
            # Import file
            dfs = pd.read_excel(path_file, sheet_name=sheet)
            # Convert df to dict
            data_dict = dfs.to_dict('records')
            # Connect to database
            mydb = self._connect_to_mongodb(database, port)
            # Insert data to retails DB
            print("########################################################")
            print("Data injection begin!")
            # drop connection to avoid inserting code many times
            mydb['collection'].drop()
            mydb['collection'].insert_many(data_dict)
            print("Data injection done successfully!")
            print("########################################################")
        except Exception as e:
            print(e)

if __name__ == "__main__":
    path_file = sys.argv[1]
    sheet_name = sys.argv[2]
    #  get using command parameters or from the environment variables
    print(sys.argv)
    if len(sys.argv) > 3:
        host = sys.argv[3]
        database = sys.argv[4]
        port = sys.argv[5]
    else:
        host = os.environ['MONGODB_IP']
        database = os.environ['MONGODB_DB']
        port = os.environ['MONGODB_PORT']

    mongo_session = mongo_data(host)
    mongo_session.inject_data_to_mongodb(path_file, sheet_name, database, port)


