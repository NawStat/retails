from pyspark.sql import SparkSession
from pyspark.sql.functions import col, desc, sum, round


def _spark_session(database, collection, ip, port=27017):
    """
    Connect to spark session
    retrun: dataframe
    """
    try:
        print("########################################################")
        print('Connecting to Spark session begin!')
        spark = SparkSession \
            .builder \
            .appName("retails_app") \
            .config("spark.mongodb.read.connection.uri",
                    "mongodb://" + ip + ":" + str(port) + "/" + database + "." + collection) \
            .config("spark.mongodb.write.connection.uri",
                    "mongodb://" + ip + ":" + str(port) + "/" + database + "." + collection) \
            .config("spark.jars.packages", "org.mongodb.spark:mongo-spark-connector:10.0.4") \
            .config("spark.driver.extraJavaOptions",
                    "-Dhttp.proxyHost=proxy.dsi.scom -Dhttp.proxyPort=8080 -Dhttps.proxyHost=proxy.dsi.scom -Dhttps.proxyPort=8080") \
            .getOrCreate()
        df = spark.read.format("mongodb").load()
        print('Spark session success !')
        print("########################################################")
        return df
    except Exception as e:
        print(e)

class spark_computations:
    """
    Perform spark computations on data from mongodb
    """
    def __init__(self, database, collection, ip, port):
        self.df = _spark_session(database, collection, ip, port)

    def group_by_field(self, field):
        """
        Group all transactions by field
        return: pyspark.sql.group.GroupedData'
        """
        return self.df.groupBy(field)
    def get_data(self):
        """
        return a collection of all data
        """
        return self.df.collect()

    def first_customer(self):
        """
        Return which customer spent the most money
        """
        return self.df.withColumn('cost', col('Quantity')*col('UnitPrice')).\
            sort(desc('cost')).limit(1).collect()[0].CustomerID

    def product_sold_most(self):
        """
        Product sold the most
        """
        return self.df.groupby('InvoiceNo').\
            agg(sum('Quantity').alias('sum_quantity')).sort(desc('sum_quantity')).limit(1).collect()[0]

    def ration_price_quantity(self):
        """
        Return the ratio between price and quantity for each invoice
        """
        data = self.df.withColumn('ratio', round(col('UnitPrice')/col('Quantity'), 3)).select('InvoiceNo', 'ratio')
        return data.collect()
