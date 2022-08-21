import os
from datetime import datetime

import apache_beam as beam

SERVICE_ACC = '/home/kiq/Stud/Data_Engineer/Beam/beam-apache-fcf078c4c4b0.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = SERVICE_ACC # Setting env variable 

pipe = beam.Pipeline()

cloud_pipe = (
    pipe
    | beam.io.ReadFromText('test.csv',skip_header_lines=1)
    | beam.Map(lambda x: x.split(','))
    | beam.Filter(lambda x: int(x[1]) < 25)
    | beam.io.WriteToText(f'gs://beam-course/age_filtered-{datetime.now()}.csv') # Saving on gcp cloud storage.
)

pipe.run()