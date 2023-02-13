from pyspark.sql import SparkSession

spark = SparkSession\
    .builder\
    .appName('Handling')\
    .getOrCreate()
    
df = spark.read.parquet('')

df.show(truncate=False)