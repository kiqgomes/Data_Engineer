import apache_beam as beam

pipe = beam.Pipeline()

# Map fn showed on basic_pipe
map_flatmap = (
    pipe
        | beam.io.ReadFromText('test.csv')
        | beam.FlatMap(lambda x: x.split(','))
        | beam.io.WriteToText('../Transformations/flatmap_item.txt')
)

pipe.run()