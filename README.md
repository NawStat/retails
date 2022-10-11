### About the project 
This is not the final version of the project, it covers :
* Data injection from xlsx file to mongodb
* Some calculations with spark engine, in our case I used the pyspark library:
    1. Group all transactions by invoice
    2. Which product sold the most?
    3. Which customer spent the most money?
    4. What is the ratio between price and quantity for each invoice?
* Basic Django web app to contain this calculations
* Dockerize the environement Django + Spark + MongoDB
### Enviroment preparation
#### Enviroment method 1
Make sure that you have installed docker and docker compose
```
git clone https://github.com/NawStat/retails.git
docker compose up 
```
It will take a while to install the requirements, inject data to mongoDB and  create the Spark session.  
when it's done open 127.0.0.1:8000
#### Enviroment method 2
This method using python virtualenv and an image of mongodb
Note: you need is to have java installed on your system PATH, or the JAVA_HOME environment variable pointing to a Java installation.
Make sure Java version is at least 8.
```
# mongo db image with volume
docker run -d -p 27017:27017 -v ~/inject_to_mongodb:/data/db --name  mongo_kinaxia mongo:latest
python3 -m venv .env 
souce .env/bin/activate
pip install -r requirements
# aAd JAVA_HOME to your environment for example JAVA_HOME="/usr/lib/jvm/java-1.11.0-openjdk-amd64"
source /etc/environment
./manage runserver 
```
####  Example to test manually the injection script file 
```
python xlsx_to_mongodb.py 'data/OnlineRetail.xlsx' 'Online Retail' '172.17.0.3' 'retails2' 27017
```
#### Example to test manually spark session 
You can user this file to test_sparksession.py to test spark connection to mongodb 