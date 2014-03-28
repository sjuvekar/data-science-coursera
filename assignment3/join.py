import MapReduce
import sys

mr = MapReduce.MapReduce()

#Mapper
def mapper(record):
	# 1st element type
	# 2nd element id
	record_type = record[0]
	id = record[1]
	mr.emit_intermediate(id, [record_type, record])

#Reducer
def reducer(key, list_of_values):
	order_list = filter(lambda a: a[0] == "order", list_of_values)
	line_item_list = filter(lambda a: a[0] == "line_item", list_of_values)
	for o in order_list:
		for l in line_item_list:
			mr.emit(o[1] + l[1])

# Part 4
inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
