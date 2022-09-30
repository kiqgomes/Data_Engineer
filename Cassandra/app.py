"""Main app
"""
import csv
import glob
import logging
import os

from pipeline import connect_cluster

logging.basicConfig(filename=f'{os.getcwd()}/log.txt',format='%(asctime) %(message)'\
                    ,level=logging.INFO)

def extracting_data():
    """
        All our etl process
    """
    logging.info("Starting the process")

    data_path = "raw_data"

    logging.info("Root processing path -> %s",data_path)

    absolute_path = []

    logging.info("Extracting the absolute path of each file")
    for root,_,_ in os.walk(data_path):
        # Will walk under all your itens on the path,
        # return the root path, your dirs and files on lists
        absolute_path = glob.glob(os.path.join(root,'*'))
    data_line_all = []

    logging.info("Consolidating all data on a unique file")
    for file_ in absolute_path:
        with open(file_,'r',encoding='utf8',newline='') as fh_:
            reader = csv.reader(fh_)
            next(reader)

            for line in reader:
                data_line_all.append(line)
    logging.info('Extraction succeed!')

    return data_line_all


def processing_data(records):
    """Processing our data

    Args:
        records (list): Result list of the extraction process
    """

    logging.info('Starting the process block!')

    csv.register_dialect('dataPattern',quoting= csv.QUOTE_ALL, skipinitialspace= True)

    logging.info('Filtering the important features')
    with open('result/consolidated_data.csv','w',encoding='utf8',newline='') as fh_: 
        writer = csv.writer(fh_)
        writer.writerow(['artist','firstName','gender','itemSession','lastName'\
            ,'length','level','location','sessionId','song','userId']) # Setting Header
        for row in records:
            if not row[0]:
                continue
            writer.writerow((row[0],row[2],row[3],row[4]\
                ,row[5],row[6],row[7],row[8],row[12],row[16]))
    logging.info('Transformation succeed!')

if __name__ == '__main__':
    records_list = extracting_data()

    if records_list:
        processing_data(records_list)

        connect_cluster()
        