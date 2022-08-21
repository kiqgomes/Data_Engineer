import csv
import logging
import os
import time

from google.cloud import pubsub_v1

logging.basicConfig(format='%(asctime)s %(message)s',level=logging.DEBUG)

SERVICE_ACC = '/home/kiq/Stud/Data_Engineer/Beam/beam-apache-fcf078c4c4b0.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = SERVICE_ACC # Setting env variable 

topic = 'projects/beam-apache/topics/Pessoas'
publisher = pubsub_v1.PublisherClient()

input_ = '/home/kiq/Stud/Data_Engineer/Beam/StreamingProjects/test.csv'

with open(input_,'rb') as f:
    for row in f:
        # print('Publishing')
        logging.info('Publishing')
        publisher.publish(topic,row)
        time.sleep(2)
