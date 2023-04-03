from airflow.decorators import dag
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.operators.python import PythonOperator
import pendulum
from datetime import timedelta
import logging as log

log.basicConfig(
    format="%(asctime)s | %(levelname)s | %(message)%",
    datefmt="%d - %M - %Y",
    level=log.INFO
)

args_ = {"owner": "airflow", "retries": 1, "retries_delay": timedelta(seconds=60)}


@dag(
    dag_id="process_improved",
    default_args=args_,
    start_date=pendulum.today().add(-1)
    # ,schedule='0 13 * * *'
    ,
    schedule="@once",
)
def main_job():
    def extract_data(**kwargs):
        import csv

        log.info("Starting extraction process")

        with open("/opt/airflow/dags/data/DIM_CLIENTE.csv", "r") as f:
            # reader = csv.reader(f) Fix Mapping problem
            reader = csv.DictReader(f)
            for l in reader:
                # data.append(tuple(l)) Fix Mapping problem
                data = dict(l)
        
        log.info(data)

        log.info("Inserting data on table of Postgres")
        
        ddl = "Insert into lab06.DIM_CLIENTE (%s) VALUES (%s)" % (",".join(data.keys()), ",".join("%s" for _ in data.keys())) 
        
        p_operator = PostgresOperator(
            task_id="load_data",
            # sql = 'Insert into lab06.DIM_CLIENTE (id_cliente,nome_cliente,sobrenome_cliente) VALUES (%s,%s,%s)', Fix Mapping problem
            sql=ddl,
            postgres_conn_id="DWFormation",
            # params = ext_op.python_callable() Fix Mapping problem
            params=(data)
        )
        p_operator.execute(context=kwargs)

    extAndsaving_data = PythonOperator(
        task_id="extractAndsave_data",
        python_callable=extract_data,
        provide_context=True,
        op_kwargs={
            "params": {"csv_file_path": "/opt/airflow/dags/data/DIM_CLIENTE.csv"}
        }
    )

    extAndsaving_data

job = main_job()
