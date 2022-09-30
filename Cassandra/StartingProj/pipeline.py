import csv
import logging
import os

import pandas as pd
from cassandra.cluster import Cluster

logging.basicConfig(filename=f'{os.getcwd()}/log.txt',format='%(asctime)s: %(message)s'\
                    ,level=logging.INFO)

if __name__ == '__main__':
    print("Don't execute, module part of the main app: app.py")

FILE_NAME = 'result/consolidated_data.csv'

def connect_cluster():
    """Create a Cassandra Cluster
    """
    cluster = Cluster(['localhost'])
    session = cluster.connect()
    session.execute("Create Keyspace If Not Exists projeto1"
                    " With Replication = { 'class': 'SimpleStrategy','replication_factor' :1 }")
    session.set_keyspace('projeto1')
    pipeline_analytics_1(session)
    drop_tables(session)
    session.shutdown()
    cluster.shutdown()
    logging.info("Pipeline succeed")

def pipeline_analytics_1(session):
    """Answer a business question
    
    Args:
        session (Cluster.connect): Set up our cassandra session
    """
    logging.info("Analytics 1 - Starting!")
    query = "Create Table If Not Exists tb_session_itemSession"
    query += "(sessionId int, itemInSession int, song int, artist text, length float, "\
            "Primary Key (sessionId, itemInSession))"
    session.execute(query)
    with open(FILE_NAME,'r',encoding='utf-8') as fh_:
        reader = csv.reader(fh_)
        next(reader) # Skip the first line
        for line in reader:
            query = "Insert Into tb_session_itemSession "\
                "(sessionId, itemInSession, song,length)"
            query += f"Values ({line[8]},{line[3]},{line[9]},{line[5]})" # ERROR TO INSERT TEXT(artists text) WITH SPACES ON CASSANDRA 4.1
            session.execute(query)
    query = "Select artist, song, length From tb_session_itemSession"\
            " Where sessionId = 436 and itemInSession = 12"
    df_ = pd.DataFrame(list(session.execute(query)))
    df_.to_csv('result/pipe1.csv',sep=',',encoding='utf-8',index=False)
    logging.info("Analytics 1 succeed")
    
def drop_tables(session):
    """Drop Tables

    Args:
        session (Cluster.connect): Set up our cassandra session
    """
    query = "Drop Table tb_session_itemSession"
    session.execute(query)
    logging.info("Table Dropped")
    