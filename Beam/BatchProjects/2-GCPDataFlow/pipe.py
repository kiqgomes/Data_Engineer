import os
from datetime import datetime

import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

pipe_options_dict = {
    'project': 'beam-apache'
    ,'runner': 'DataFlowRunner'
    ,'region': 'southamerica-east1'
    ,'staging_location': 'gs://staging-beam-ap/'
    ,'temp_location': 'gs://staging-beam-ap/temp/'
    ,'template_location': 'gs://beam-course/templates/batch_job_dataflow' # Will be used to import and run my code on DataFlow
}


SERVICE_ACC = '/home/kiq/Stud/Data_Engineer/Beam/beam-apache-fcf078c4c4b0.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = SERVICE_ACC 

pipe_options = PipelineOptions.from_dictionary(pipe_options_dict)

pipe = beam.Pipeline(options=pipe_options)

dl_pipe = (
    pipe
    | beam.io.ReadFromText('gs://input-beam/test.csv',skip_header_lines=1)
    | beam.Map(lambda x: x.split(','))
    | beam.Map(lambda x: (x[0],x[2]))
    | beam.combiners.Count.PerKey()
    | beam.io.WriteToText(f'gs://curated-beam/name_count-{datetime.now()}.csv')
    # | beam.Map(print)
)

pipe.run()