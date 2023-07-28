// Databricks notebook source
dbutils.fs.mkdirs("/mnt/data")

// COMMAND ----------

dbutils.fs.ls("/mnt")

// COMMAND ----------


val configs = Map(
  "fs.azure.account.auth.type" -> "OAuth",
  "fs.azure.account.oauth.provider.type" -> "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
  "fs.azure.account.oauth2.client.id" -> "",
  "fs.azure.account.oauth2.client.secret" -> "",
  "fs.azure.account.oauth2.client.endpoint" -> "https://login.microsoftonline.com//oauth2/token")
dbutils.fs.mount(
  source = "abfss://base@datalakekiq.dfs.core.windows.net/",
  mountPoint = "/mnt/data",
  extraConfigs = configs)

// COMMAND ----------

dbutils.fs.ls("/mnt/data")

// COMMAND ----------


