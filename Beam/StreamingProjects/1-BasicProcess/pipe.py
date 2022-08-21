import os
from datetime import datetime

import apache_beam as beam
from apache_beam import window
from apache_beam.options.pipeline_options import PipelineOptions

pipe_options_dict = {
    'project': 'beam-apache'
    ,'runner': 'DataFlowRunner'
    ,'region': 'southamerica-east1'
    ,'staging_location': 'gs://staging-beam-ap/'
    ,'temp_location': 'gs://staging-beam-ap/temp/'
    ,'template_location': 'gs://beam-course/templates/streaming_job_pubsub_final' # Will be used to import and run my code on DataFlow
    ,'save_main_session': True # To use my custom fn
    ,'streaming': True
}

SERVICE_ACC = '/home/kiq/Stud/Data_Engineer/Beam/beam-apache-fcf078c4c4b0.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = SERVICE_ACC

SUBSCRIPTION = 'projects/beam-apache/subscriptions/Pessoas-sub'
OUTPUT = 'projects/beam-apache/topics/Streaming_output'

pipe_options = PipelineOptions.from_dictionary(pipe_options_dict)

# class Decoder(beam.DoFn):
#     def decode(self,record):
#         return [record.decode('utf-8').split(',')]

pipe = beam.Pipeline(options= pipe_options)

streaming_pipe = (
    pipe
    | beam.io.ReadFromPubSub(subscription=SUBSCRIPTION)
    # | "Decoding and spliting" >> beam.ParDo(Decoder()) # Pub/sub items be only transported on bytes
    | "Decoding w/ Map" >> beam.Map(lambda x: x.decode('utf-8'))
    | "Splitting " >> beam.Map(lambda x: x.split(',')) 
    | beam.Map(lambda x: (x[0],x[2])) # Setting to a tuple
    # | "Setting window" >> beam.WindowInto(window.SlidingWindows(10,5)) # Create a window of 10 seconds and create others 5 per 5 seconds
    | "Setting window" >> beam.WindowInto(window.FixedWindows(5)) # Fixed window of 5 seconds
    | "Summing items" >> beam.combiners.Count.PerKey()
    | "Transforming in bytes" >> beam.Map(lambda x: (''.join(str(x)).encode('utf-8'))) # Pub/sub items be only transported on bytes
    | "Serving the PubSub" >> beam.io.WriteToPubSub(OUTPUT)
)

result = pipe.run()
result.wait_until_finish() # Run until I don't stop the job on the runner