import csv
import pandas 
from cassandra.cluster import Cluster

if __name__ == '__main__':
    print("Don't execute, module part of the main app: app.py")

file_name = 'result/consolidated_data.csv'

def connect_cluster():
    """Create a Cassandra Cluster
    """
    cluster = Cluster(['localhost'])
    session = cluster.connect()
    session.execute("Create Keyspace If Not Exists projeto1"
                    "With Replication = { 'class': 'SimpleStrategy','replication_factor' :1 }")
    session.set_keyspace('projeto1')
    pipeline_analytics_1(session)
    pipeline_analytics_2(session)
    pipeline_analytics_3(session)
    
    
    
