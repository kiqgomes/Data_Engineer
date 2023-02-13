"""
    Read the data and show
"""
from pyspark.sql import SparkSession
from pyspark.sql import functions as f

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

words = lines\
        .select(
            f.explode(
                    f.split(lines.value,' ')
                    ).alias('word'))
        
word_counts = words.groupBy('word').count().orderBy('count',ascending=False)

q = word_counts\
    .writeStream\
    .outputMode('complete')\
    .format('console')\
    .start()

q.awaitTermination()
