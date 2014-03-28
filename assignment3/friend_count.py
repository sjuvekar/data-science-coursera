import MapReduce
import sys

mr = MapReduce.MapReduce()

#Mapper
def mapper(record):
	person = record[0]
	friend = record[1]
	mr.emit_intermediate(person, friend)

#Reducer
def reducer(key, list_of_values):
	mr.emit( (key, len(set(list_of_values))) )	

# Part 4
inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
