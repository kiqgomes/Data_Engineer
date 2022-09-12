import getopt
import sys
import time

import colorama
from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql import functions as Func


def initS():
    sc = SparkContext(appName='App2')
    spark = SparkSession.builder\
            .appName('App2')\
            .getOrCreate()
    return spark

def input_instructions():

    opts, args = getopt.getopt(sys.argv[1:],"f:l:w:")
    fformat, fload, fwrite = "","",""

    for opt,arg in opts:
        if opt == '-f':
            fformat = arg
        elif opt == '-l':
            fload = arg
        elif opt == '-w':
            fwrite = arg

    return fformat,fload,fwrite


def data_transformation(spark: SparkSession,fformat,fload):

    df = spark.read.format(fformat).load(fload)
    df_vendas_cidade = df.groupBy('cidade').agg(Func.sum('vendas').alias('vendas'))    
    return df_vendas_cidade.show()

if __name__ == "__main__":

    print(colorama.Fore.GREEN + 'Starting the app')
    for i in range(10):
        time.sleep(i/100)
        print('-'*i,end='')
    print('\n')

    spark = initS()
    
    fformat,fload,fwrite = input_instructions()

    print(colorama.Fore.BLUE + 'Results: ')
    data_transformation(spark,fformat,fload)

    spark.stop()    