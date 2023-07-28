// Databricks notebook source
dbutils.fs.mkdirs("/mnt/data")

// COMMAND ----------

dbutils.fs.ls("/mnt")

// COMMAND ----------


val configs = Map(
  "fs.azure.account.auth.type" -> "OAuth",
  "fs.azure.account.oauth.provider.type" -> "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
  "fs.azure.account.oauth2.client.id" -> "cb40893a-f218-4e92-a3f9-daec6772b754",
  "fs.azure.account.oauth2.client.secret" -> "uKN8Q~HAv3osrjrjZcIX1wS-22ln.G~ZuWpzNbkh",
  "fs.azure.account.oauth2.client.endpoint" -> "https://login.microsoftonline.com/a3bf4c1e-d28c-4cbb-ba23-404a8c032b4a/oauth2/token")
dbutils.fs.mount(
  source = "abfss://base@datalakekiq.dfs.core.windows.net/",
  mountPoint = "/mnt/data",
  extraConfigs = configs)

// COMMAND ----------

dbutils.fs.ls("/mnt/data")

// COMMAND ----------


