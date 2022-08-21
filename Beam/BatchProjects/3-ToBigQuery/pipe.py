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
    ,'template_location': 'gs://beam-course/templates/batch_job_dataflow_BQ' # Will be used to import and run my code on DataFlow
    ,'save_main_session': True # To use my custom fn
}

SERVICE_ACC = '/home/kiq/Stud/Data_Engineer/Beam/beam-apache-fcf078c4c4b0.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = SERVICE_ACC

def to_dict(x): # We need to transform data on key:value to save on BigQuery
    """
        Create a dict by a tuple of data.
    """
    dict_data = {}
    dict_data['Name'] = x[0]
    dict_data['Count'] = x[1]
    return dict_data

TABLE_SCHEMA = 'Name:STRING,Count:INTEGER' # To specify the column and the type on the BigQuery
TABLE = 'beam-apache:saving_bigquery.saving_bigquery_table'

pipe_options = PipelineOptions.from_dictionary(pipe_options_dict)

pipe = beam.Pipeline(options=pipe_options)

dl_pipe = (
    pipe
    | beam.io.ReadFromText('gs://input-beam/test.csv',skip_header_lines=1)
    | beam.Map(lambda x: x.split(','))
    | beam.Map(lambda x: (x[0],x[2]))
    | beam.combiners.Count.PerKey()
    | "Transforming my data" >> beam.Map(lambda x: to_dict(x)) # This name between "" will naming the items on the Dataflow Dag
    | "Writing on BigQuery" >> beam.io.WriteToBigQuery(table=TABLE
                                                        ,schema=TABLE_SCHEMA
                                                        ,write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND
                                                        ,create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED
                                                        ,custom_gcs_temp_location='gs://staging-beam-ap/temp')
    # | beam.Map(print)
)

pipe.run()