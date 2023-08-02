// Databricks notebook source
val path = "dbfs:/mnt/data/staging/stg_imoveis_dados"
val data = spark.read.format("delta").load(path)

// COMMAND ----------

display(data)

// COMMAND ----------

val explode_ = data.select("anuncio.*","anuncio.endereco.*")
display(explode_)

// COMMAND ----------

val tr_data = explode_.drop("endereco","caracteristicas")
display(tr_data)

// COMMAND ----------

val save_path = "dbfs:/mnt/data/trusted/tr_imoveis_dados"
tr_data.write.format("delta").mode("overwrite").save(save_path)
