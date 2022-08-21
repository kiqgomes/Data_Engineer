from ast import Subscript
import csv
import logging
import os
import time

from google.cloud import pubsub_v1

logging.basicConfig(format='%(asctime)s %(message)s',level=logging.DEBUG)

SERVICE_ACC = '/home/kiq/Stud/Data_Engineer/Beam/beam-apache-fcf078c4c4b0.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = SERVICE_ACC # Setting env variable 

SUBSCRIPTION = 'projects/beam-apache/subscriptions/beam-consumer'
subscriber = pubsub_v1.SubscriberClient()

def show_message(message):
    logging.info('Message: %s',message)
    message.ack() # ack = acknowledgement, shows to the topic, that i know about this message, and I don't need to receive anymore

subscriber.subscribe(SUBSCRIPTION,callback=show_message) # callback is to use some custom def on the consume process

while True:
    time.sleep(3)
