# !pip install -q apache-beam # Normal installation
# !pip install -q apache-beam[interactive] # More useful on notebooks
# !pip install -q apache-beam[gcp] # Will install some useful gcp libs

import apache_beam as beam

pipe = beam.Pipeline()

first_pipe = ( # first_pipe is a named Pcollection, saving in a variable to be used before 
    pipe
    | beam.io.ReadFromText('test.csv')
    | beam.Map(lambda x: x.split(','))
    | beam.io.WriteToText('../Transformations/map.txt')
)

pipe.run()