from airflow.decorators import dag
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.operators.python import PythonOperator
import pendulum
from datetime import timedelta
import logging as log

log.basicConfig(format='%(asctime)s | %(levelname)s | %(message)%',datefmt='%d - %M - %Y',level=log.INFO)

args_ = {
    'owner': 'airflow'
    ,'retries': 1
    ,'retries_delay': timedelta(seconds=60)
}

@dag(dag_id='process_improved'
         ,default_args=args_
         ,start_date=pendulum.today().add(-1)
        # ,schedule='0 13 * * *'
        ,schedule='@once')
    
def main_job():
    def extract_data():
        import csv
            
        log.info('Starting extraction process')
        data = []
            
        with open('/opt/airflow/dags/data/DIM_CLIENTE.csv','r') as f:
            reader = csv.reader(f)
            for l in reader:
                data.append(tuple(l))
        return data
    
    ext_op = PythonOperator(task_id = 'extract_data',python_callable=extract_data)
               
    log.info('Inserting data on table of Postgres')

    saving_data = PostgresOperator(
        task_id = 'load_data',
        sql = 'Insert into lab06.DIM_CLIENTE (id_cliente,nome_cliente,sobrenome_cliente) VALUES (%s,%s,%s)',
        postgres_conn_id= 'DWFormation',
        params = ext_op.python_callable()
    )
    saving_data

test = main_job()
