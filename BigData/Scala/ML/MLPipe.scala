import org.apache.spark.sql.SparkSession

import org.apache.log4j._
//Logger.getLogger("org").setLevel(Level.ERROR)

val spark = SparkSessiom.builder().getOrCreate()

import org.apache.spark.ml.KMeans

val df = spark.read.option("header","true").option("inferSchema","true").csv("data.csv")

