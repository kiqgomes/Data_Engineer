"""
 Connection module to be used by a DW creator script.
 Author: Kaique Gomes
"""

import logging
import sys

import mysql.connector as mconn

logging.basicConfig(format='%(asctime)s %(message)s',filename='connect.log'\
                    ,encoding='utf-8', level=logging.DEBUG)

logging.info("Starting connection to MySQL")

try:
    conn = mconn.connect(host='localhost',user='airflow',\
    password='Kaka2014.',database='DWengAirflow')
    logging.info("Connected to MySQL")
except Exception as ex:
    logging.error("Failed to connect to MySQL: %s",ex)
    sys.exit()
finally:
    logging.info("Connection module finalized!")
cursor = conn.cursor()
logging.info("Cursor initialized")


#   DDl (Create) SQL scripts
#    Author: DSA

cursor.execute("""
                    CREATE TABLE IF NOT EXISTS tb_prices_rang(
                        id INT PRIMARY KEY NOT NULL AUTO_INCREMENT
                        ,pricerange VARCHAR (30)
                        ,rankingposition INT
                    )
                """
                )

# Dimensão com prêmios (awards) e avaliação de usuário (rating)
cursor.execute("""
                    CREATE TABLE IF NOT EXISTS tb_hotels(
                        id INT PRIMARY KEY NOT NULL AUTO_INCREMENT
                        ,name VARCHAR (100)
                        ,awards INT
                        ,rating DOUBLE 
                    )
               """
               )

# Dimensão com número de avaliações (numberofreviews), classe do hotel (hotelclass) e avaliação de usuário (rating)
cursor.execute("""
                    CREATE TABLE IF NOT EXISTS tb_hotel_reviews(
                        id INT PRIMARY KEY NOT NULL AUTO_INCREMENT
                        ,numberofreviews INT
                        ,hotelclass DOUBLE
                        ,rating DOUBLE 
                    )
               """
               )

# Cria a tabela FATO com as chaves estrangeiras e os fatos
# print("\nCriando tabela fato...")
cursor.execute("""
                CREATE TABLE IF NOT EXISTS tb_fact(
                    pricesrange_id INT
                    ,hotels_id INT
                    ,reviews_id INT
                    ,number_of_hotels INT
                    ,number_ofrange_prices INT
                    ,max_hotelclass INT
                    ,min_hotelclass INT
                    ,max_ofreviews INT
                    ,min_ofreviews INT
                    ,KEY pricesrange_id (pricesrange_id)
                    ,KEY hotels_id (hotels_id)
                    ,KEY reviews_id (reviews_id)
                    ,CONSTRAINT fact_ibfk_1 FOREIGN KEY (pricesrange_id) REFERENCES tb_prices_rang (id)
                    ,CONSTRAINT fact_ibfk_2 FOREIGN KEY (hotels_id) REFERENCES tb_hotels (id)
                    ,CONSTRAINT fact_ibfk_3 FOREIGN KEY (reviews_id) REFERENCES tb_hotel_reviews (id))
                """
               )
# print("\nEstrutura do DW criada com sucesso!\n")
