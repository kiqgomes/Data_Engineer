// Project of a Pipeline that serve data to a NLP Model

import org.apache.spark.ml.Pipeline
import org.apache.spark.sql.{DataFrame,SparkSession}
import org.apache.spark.sql.types.{IntegerType, LongType, StringType, StructField, StructType}
import org.apache.spark.sql.functions._
import org.apache.spark.ml.linalg.{Vector, Vectors}
import org.apache.spark.ml.feature._

val spark = SparkSession.builder().master("local").appName("Pipe").getOrCreate()

// To convert RDD to DataFrame
import spark.implicits._