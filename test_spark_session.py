from pyspark.sql.functions import col, when, desc, sum

from pyspark.sql import SparkSession
spark = SparkSession \
    .builder \
    .appName("retails_app") \
    .config("spark.mongodb.read.connection.uri", "mongodb://172.17.0.3:27017/retails.collection") \
    .config("spark.mongodb.write.connection.uri", "mongodb://172.17.0.3:27017/retails.collection") \
    .config("spark.jars.packages","org.mongodb.spark:mongo-spark-connector:10.0.4")\
    .config("spark.driver.extraJavaOptions","-Dhttp.proxyHost=proxy.dsi.scom -Dhttp.proxyPort=8080 -Dhttps.proxyHost=proxy.dsi.scom -Dhttps.proxyPort=8080")\
    .getOrCreate()
df = spark.read.format("mongodb").load()