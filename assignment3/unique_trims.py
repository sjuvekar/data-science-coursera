import MapReduce
import sys

mr = MapReduce.MapReduce()

#Mapper
def mapper(record):
	seqid = record[0]
	seq = record[1]
	trimmed_seq = seq[0:-10]
	mr.emit_intermediate(trimmed_seq, seqid)

#Reducer
def reducer(key, list_of_values):
	mr.emit( key )	

# Part 4
inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
