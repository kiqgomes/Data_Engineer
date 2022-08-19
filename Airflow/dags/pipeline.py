import json

import pandas as pd
import pendulum
from airflow.models import DAG
from airflow.operators.python import PythonOperator

import connect_mysql.connect as conn

input_data = 'data/dados_hoteis.json'

def data_load():
    """
        Read and save the json file
    """
    with open(input_data,'r',encoding='UTF-8') as f:
        data = json.load(f)
    return data

def extract_attributes(path: str):
    """
        Extract all data from loaded json (var -> data).
        And save on a Dataframe.
    """
    data = data_load()
    list_data = []

    try:
        for l in data:
            list_data.append({'ID': l['id']
                            ,'Name': l['name']
                            ,'Type': l['type']
                            ,'rating': l['rating']
                            ,'Awards': len(l['awards'])
                            ,'RankingPosition': l['rankingPosition']
                            ,'HotelClass': l['hotelClass']
                            ,'NumberOfReviews': l['numberOfReviews']
                            ,'priceRange': l['priceRange']
                            })
    except:
        print("Error to list data.")
        pass

    df = pd.DataFrame(list_data)

    df.to_csv(path,index=False)

def extract_prices_and_range(path: str):
    """
        Extract prices and range from loaded json (var -> data).
        And save on a Dataframe.
    """
    data = data_load()

    list_data = []

    try:
        for l in data:
            list_data.append({'priceRange': l['priceRange']
                            ,'RankingPosition': l['rankingPosition']
                            })
    
    except:
        print("Error to list data.")
        pass

    df_pAndr = pd.DataFrame(list_data)
    df_pAndr.to_csv(path,index=False)

def extract_hotel_award_rating(path: str):
    """
        Extract hotel name, award (qtd.), rating from loaded json (var -> data).
        And save on a Dataframe.
    """
    data = data_load()

    list_data = []

    try:
        for l in data:
            list_data.append({'Name': l['name']
                            ,'Awards': len(l['awards'])
                            ,'rating': l['rating']
                            })
    except:
        print("Error to list data.")
        pass

    df_har = pd.DataFrame(list_data)
    df_har.to_csv(path,index=False) 

def extract_hotel_class(path: str):
    """
        Extract hotel class, number of reviews and rating from loaded json (var -> data).
        And save on a Dataframe.
    """
    data = data_load()

    list_data = []

    try:
        for l in data:
            list_data.append({'HotelClass': l['hotelClass']
                            ,'NumberOfReviews': l['numberOfReviews']
                            ,'rating': l['rating']
                            })
    except:
        print("Error to list data.")
        pass

    df_hc = pd.DataFrame(list_data)
    df_hc.to_csv(path,index=False) 
    
def upload_dim():
    """
        Upload the extracted data to dimensions on DB.
    """

    data_dim1 = pd.read_csv('/data/result2.csv',index_col=False)
    data_dim1.head()

    sql = 'SET SQL_SAFE_UPDATES = 0'
    conn.cursor.execute(sql)
    conn.conn.commit()

    sql = 'TRUNCATE TABLE tb_prices_rang'
    conn.cursor.execute(sql)
    conn.conn.commit()

    for i,row in data_dim1.iterrows():
        sql = "INSERT INTO tb_prices_rang(pricerange,rankingposition) VALUES (%s,%s)"
        conn.cursor.execute(sql,tuple(row))
        conn.conn.commit()

    data_dim2 = pd.read_csv('/data/result3.csv',index_col=False)
    data_dim2.head()

    sql = 'TRUNCATE TABLE tb_hotels'
    conn.cursor.execute(sql)
    conn.conn.commit()

    for i,row in data_dim2.iterrows():
        sql = "INSERT INTO tb_hotels(name,awards,rating) VALUES (%s,%s,%s)"
        conn.cursor.execute(sql,tuple(row))
        conn.conn.commit()

    data_dim3 = pd.read_csv('/data/result4.csv',index_col=False)
    data_dim3.head()

    sql = 'TRUNCATE TABLE tb_hotels_reviews'
    conn.cursor.execute(sql)
    conn.conn.commit()

    for i,row in data_dim2.iterrows():
        sql = "INSERT INTO tb_hotels_reviews(numberofreviews,hotelclass,rating) VALUES (%s,%s,%s)"
        conn.cursor.execute(sql,tuple(row))
        conn.conn.commit()

def upload_fact():
    """
        Consolidate the fact table.
    """
    sql = 'TRUNCATE TABLE tb_fact'
    conn.cursor.execute(sql)
    conn.conn.commit()

    sql = """
            INSERT INTO tb_fact(
                pricesrange_id
                ,hotels_id
                ,reviews_id
                ,number_of_hotels
                ,number_ofrange_prices
                ,max_hotelclass
                ,min_hotelclass
                ,max_ofreviews
                ,min_ofreviews
                )
            Select tb_prices_rang.id
                ,tb_hotels.id
                ,tb_hotel_reviews.id
                ,count(name)
                ,count(pricerange)
                ,max(hotelclass)
                ,min(hotelclass)
                ,max(numberofreviews)
                ,min(numberofreviews)
            FROM tb_prices_rang
                ,tb_hotels
                ,tb_hotel_reviews
            GROUP BY tb_prices_rang.id
                ,tb_hotels.id
                ,tb_hotel_reviews.id;
        """

    conn.cursor.execute(sql)
    conn.conn.commit()

    sql = "SET SQL_SAFE_UPDATES = 1"
    conn.cursor.execute(sql)
    conn.conn.commit()


# Really Airflow, open a DAG and code to execute us defs and on the final set the execution order


with DAG(dag_id = 'DAG_DW', start_date = pendulum.datetime(2022,1,1,tz="UTC")\
        ,schedule_interval = '@Daily',catchup=False) as dag:
    task1_data_load = PythonOperator(
        task_id = 'data_load'
        ,python_callable= data_load
        ,dag= dag
    )

    task2_extract_attributes = PythonOperator(
        task_id = 'extract_attributes'
        ,python_callable= extract_attributes
        ,op_kwargs= {'path':'data/result1.csv'}
        ,dag= dag
    )
    task3_extract_prices_and_range = PythonOperator(
        task_id = 'extract_prices_and_range'
        ,python_callable= extract_prices_and_range
        ,op_kwargs= {'path':'data/result2.csv'}
        ,dag= dag
    )
    task4_extract_hotel_award_rating = PythonOperator(
        task_id = 'extract_hotel_award_rating'
        ,python_callable= extract_hotel_award_rating
        ,op_kwargs= {'path':'data/result3.csv'}
        ,dag= dag
    )
    task5_extract_hotel_class = PythonOperator(
        task_id = 'extract_hotel_class'
        ,python_callable= extract_hotel_class
        ,op_kwargs= {'path':'data/result4.csv'}
        ,dag= dag
    )
    task6_upload_dim = PythonOperator(
        task_id = 'upload_dim'
        ,python_callable= upload_dim
        ,dag= dag
    )
    task7_upload_fact = PythonOperator(
        task_id = 'upload_fact'
        ,python_callable= upload_fact
        ,dag= dag
    )
    task1_data_load >> task2_extract_attributes >> task3_extract_prices_and_range \
    >> task4_extract_hotel_award_rating >> task5_extract_hotel_class >> task6_upload_dim >> task7_upload_fact