import apache_beam as beam

pipe = beam.Pipeline()

filter_fn = (
    pipe
        | beam.io.ReadFromText('test.csv')
        | beam.Map(lambda x: x.split(','))
        | beam.Filter(lambda x: x[0] == 'Kaique')
        | beam.Map(print)
)

pipe.run()