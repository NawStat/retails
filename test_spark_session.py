from pyspark.sql.functions import col, when, desc, sum
from pyspark.sql import SparkSession

ip = "192.168.144.2"
ip = "mongo"
spark = SparkSession \
    .builder \
    .appName("retails_app") \
    .config("spark.mongodb.read.connection.uri", "mongodb://"+ip+"/retails2.collection") \
    .config("spark.mongodb.write.connection.uri", "mongodb://"+ip+"/retails2.collection") \
    .config("spark.jars.packages","org.mongodb.spark:mongo-spark-connector:10.0.4")\
    .config("spark.driver.extraJavaOptions","-Dhttp.proxyHost=proxy.dsi.scom -Dhttp.proxyPort=8080 -Dhttps.proxyHost=proxy.dsi.scom -Dhttps.proxyPort=8080")\
    .getOrCreate()
df = spark.read.format("mongodb").load()
stockid = 22728
d = df.where(df.StockCode == stockid).groupby('Country').sum('Quantity').withColumnRenamed("SUM(Quantity)", "Total Quantity")
d = df.filter(df.StockCode == stockid).groupby('Country').sum('Quantity'). \
    withColumnRenamed("SUM(Quantity)", "Total Quantity")
p = d.toPandas()
p = p.set_index('Country')
img = p.plot.pie(y='Total Quantity', figsize=(10, 10), autopct='%.2f', labeldistance=None,
                 title='Product distribution by country')
img.get_figure().savefig(str(stockid))
