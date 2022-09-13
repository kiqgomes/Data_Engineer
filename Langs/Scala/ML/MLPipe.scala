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

// Importing vectors to model data and made be useful to Spark ML
// The data needs to be in Vector on all (or almost) Spark ML models options 
import org.apache.spark.ml.feature.{VectorAssembler,StringIndexer,VectorIndexer,OneHotEncoder}
import org.apache.spark.ml.linalg.Vectors

// Assembler receive the VectorAssembler object
val assembler = new VectorAssembler()
                    .setInputCols(Array("Fresh","Milk","Grocery","Frozen"
                    ,"Detergents_Paper","Delicatessen"))
                    .setOutputCol("features")

// And we use the assemble to transform our feature_data  
val dataset = assembler
                .transform(feature_data)                
                .select("features")

// Setting up out model Kmeans with a K=3 
// K = Number of clusters (or group) that the data will bem separated
val kmeans = new KMeans()
                    .setK(3) // Kmeans hyperparameter
                    .setSeed(1L) // Seed to that our model can be reproduced

// Training the model
val model = kmeans.fit(dataset)

val predict = model.transform(dataset)

// Declaring the cluster (or group) evaluator
val evaluator = new ClusteringEvaluator()

// Silhouette is a score that evaluate the cluster, result can be between -1 and 1
// Being near 1 -> dense cluster and really separated
// Near 0 -> overlapping cluster
// Less than 0 -> data probably wrong or incorrect 
val silhouette = evaluator.evaluate(predict)
println(s"Silhouette Score = $silhouette")

// Show results
println("Client Subjects (Clusters): ")
predict.collect().foreach(println)

// Save results
import java.io._
val writer = new BufferedWriter(new FileWriter("predict.txt"))
predict.collect().foreach(x=>{writer.write(x.toString())})
writer.close()