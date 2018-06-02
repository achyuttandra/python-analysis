# import data file in JSON format
path = "/FileStore/tables/2015q3.json"
data = spark.read.option("multiline", "true").json("/FileStore/tables/2015q3.json")
data.take(20)
