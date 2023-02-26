from datetime import timedelta
import pendulum
from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator

args = {'owner':'airflow'}

default_args = {
    'owner':'airflow'
    ,'retries': 1
    ,'retry_delay': timedelta(minutes=5)
}

dag_lab = DAG(dag_id= 'lab'
              ,default_args=args
              ,schedule_interval='@once'
              ,dagrun_timeout=timedelta(minutes=60)
              ,description='ETL with airflow'
              ,start_date=pendulum.today().add(-1))

start = EmptyOperator(task_id='start')

sql_ddl = """ Create Table If Not Exists dwdsa.tb_employees (id INT NOT NULL, name VARCHAR(250) NOT NULL,department VARCHAR(250) NOT NULL);"""

create_table = PostgresOperator(sql = sql_ddl
                                ,task_id = 'create_table'
                                ,postgres_conn_id = 'DWFormation'
                                ,dag = dag_lab                            
)

sql_dml = """ Insert into dwdsa.tb_employees (id,name,department) Values (1,'Kaique','Data Engineer'),(2,'Kaique Too','Data Scientist')""" 

insert_data = PostgresOperator(sql = sql_dml
                                ,task_id = 'insert_data'
                                ,postgres_conn_id = 'DWFormation'
                                ,dag = dag_lab                        
)

end = EmptyOperator(task_id='end')

#Dag Flow

start >> create_table >> insert_data >> end

if __name__ == '__main__':
    dag_lab.cli()
    