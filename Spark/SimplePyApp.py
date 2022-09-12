import sys

from pyspark import SparkContext
from pyspark.sql import SparkSession


def initS():
    sc = SparkContext(appName='App')
    spark = SparkSession.builder\
        .master('local')\
        .appName('App')\
        .getOrCreate()
    return spark

def data_transformation(spark: SparkSession):
    df = spark.read.format('parquet').load(sys.argv[1])
    df.show()

if __name__ == '__main__':
    spark = initS()
    data_transformation(spark)

    spark.stop()