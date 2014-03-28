import MapReduce
import sys

mr = MapReduce.MapReduce()

#Mapper
def mapper(record):
	person = record[0]
	friend = record[1]
	if person < friend:
		mr.emit_intermediate((person, friend), friend)
	else:
		mr.emit_intermediate((friend, person), friend)
		
#Reducer
def reducer(key, list_of_values):
	first_confirmed = False
	second_confirmed = False
	for v in list_of_values:
		if v == key[0]:
			first_confirmed = True
		if v == key[1]:
			second_confirmed = True
	if not (first_confirmed and second_confirmed):
		mr.emit( (key[0], key[1]) )
		mr.emit( (key[1], key[0]) ) 

# Part 4
inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
