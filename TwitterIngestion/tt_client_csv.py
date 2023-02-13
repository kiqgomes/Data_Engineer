"""
    Read the data and show
"""
from pyspark.sql import SparkSession
import shutil

for p in ['./db','./db/ckeckpoint']:
    try:
        shutil.rmtree(p)
    except OSError as ex:
        print(f"Error on delete paths\n{ex}")


spark = SparkSession\
    .builder\
    .appName('TwitterAPI')\
    .master('local')\
    .getOrCreate()

lines = spark\
    .readStream\
    .format('socket')\
    .option('host','localhost')\
    .option('port',3001)\
    .load()

q = lines\
    .writeStream\
    .outputMode('append')\
    .format('csv')\
    .option('path','./db/')\
    .option("checkpointLocation", "./db/ckeckpoint/")\
    .start()

q.awaitTermination()
