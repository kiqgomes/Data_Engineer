import org.apache.spark.sql.SparkSession

import org.apache.log4j._
Logger.getLogger("org").setLevel(Level.WARN)

// Creating the Spark Session
val spark = SparkSession
            .builder()
            .getOrCreate()

import org.apache.spark.ml.KMeans // Import the model from Spark ML

// Reading the Data
val df = spark.read
        .option("header","true") // Reading the header
        .option("inferSchema","true") // Inferring a data schema
        .csv("data.csv") // Data Type

// Selecting the columns to train model
val feature_data = df.select($"Fresh",$"Milk",$"Grocery"
                            ,$"Frozen",$"Detergents_Paper",$"Delicatessen")
println(df.schema)

// Importing models
import org.apache.spark.ml.feature.{VectorAssembler,StringIndexer,VectorIndexer,OneHotEncoder}
import org.apache.spark.ml.linalg.Vectors