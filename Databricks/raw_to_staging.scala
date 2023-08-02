// Databricks notebook source
val path = "dbfs:/mnt/data/raw/dados_brutos_imoveis.json"
val data = spark.read.json(path)

// COMMAND ----------

display(data)

// COMMAND ----------

val cleanded_dataset = data.drop("imagens","usuario")

// COMMAND ----------

display(cleanded_dataset)

// COMMAND ----------

import org.apache.spark.sql.functions.col

// COMMAND ----------

val stg_data = cleanded_dataset.withColumn("id",col("anuncio.id"))
display(stg_data)

// COMMAND ----------

val save_path = "dbfs:/mnt/data/staging/stg_imoveis_dados"
stg_data.write.format("delta").mode("overwrite").save(save_path)

// COMMAND ----------

dbutils.fs.ls("/mnt/data/staging/")
