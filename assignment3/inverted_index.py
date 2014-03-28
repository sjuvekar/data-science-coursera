import MapReduce
import sys

mr = MapReduce.MapReduce()

#Mapper
def mapper(record):
	docid = record[0]
	text = record[1]
	words = text.split()
	for w in words:
		mr.emit_intermediate(w, docid)

#Reducer
def reducer(key, list_of_values):
	mr.emit( (key, list(set(list_of_values))) )	

# Part 4
inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
