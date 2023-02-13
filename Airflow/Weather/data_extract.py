"""Extract weather data with Airflow
"""
from airflow.models import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
import pendulum
from datetime import datetime,timedelta
from os.path import join
import pandas as pd
import os
import secrets_weather_api

CITY = 'Belo-Horizonte'
KEY = secrets_weather_api.KEY
DATA_INICIO = datetime.now()
DATA_FIM = DATA_INICIO + timedelta(7)
DATA_INICIO = DATA_INICIO.strftime('%Y-%m-%d')
DATA_FIM = DATA_FIM.strftime('%Y-%m-%d')

def data_extract(air_data_end):
    """Def to extract data
    """
    URI = join("https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/",
            f"{CITY}/{DATA_INICIO}/{DATA_FIM}?unitGroup=metric&include=days&key={KEY}&contentType=csv")
    data = pd.read_csv(URI)
    print(data.head())
    print(os.getcwd())
    output_dir = f'{os.getcwd()}' + f'/{air_data_end}'
    print(output_dir)

    os.mkdir(output_dir)
    data.to_csv(output_dir + "/raw_data_7days.csv",index=False)


with DAG(
    'weather_extract',
    schedule_interval='0 0 * * 1', # Weekly run
    start_date=pendulum.today('UTC').add(days=-1)
    ) as dag:
    task_0 = EmptyOperator(task_id='start')
    task_00 = EmptyOperator(task_id='end')
    task_1 = PythonOperator(
        task_id = 'data_extract',
        python_callable=data_extract,
        op_kwargs={'air_data_end': '{{data_interval_end.strftime("%Y-%m-%d")}}'})
    task_0 >> task_1 >> task_00
