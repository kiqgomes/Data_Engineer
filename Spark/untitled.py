import sys,getopt
from pyspark.sql import SparkSession
from pyspark import SparkContext

def init():
    sc = SparkContext(appName='App')
    spark = SparkSession.builder\
        .master('local')\
        .appName('App')\
        .getOrCreate()
return spark

def data_transformation(spark: SparkSession):
    df = spark.read.format('parquet').load(sys.argv)