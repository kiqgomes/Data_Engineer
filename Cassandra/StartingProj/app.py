import csv
import glob
import logging
import os

logging.basicConfig(filename='./log.txt',format='%(asctime) %(message)'\
                    ,level=logging.INFO)

def etl_process():
    """
        All our etl process
    """
    logging.info("Starting the process")

    data_path = "data_raw"

    logging.info("Root processing path -> %s",data_path)

    absolute_path = []

    logging.info("Extracting the absolute path of each file")

    for root,dirs,files in os.walk(data_path):
        absolute_path = glob.glob(os.path.join(root,'*'))

    