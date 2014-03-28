import MapReduce
import sys

mr = MapReduce.MapReduce()
max_dim = 10

#Mapper
def mapper(record):
	mat_name = record[0]
	row = record[1]
	col = record[2]
	value = record[3]
	if mat_name == "a":
		for col_id in range(max_dim):
			mr.emit_intermediate( (row, col_id), ["a", [col, value]] )
	else:
		for row_id in range(max_dim):
			mr.emit_intermediate( (row_id, col), ["b", [row, value]] )	

#Reducer
def reducer(key, list_of_values):
	a_list = filter(lambda a:a[0] == "a", list_of_values)
	b_list = filter(lambda a:a[0] == "b", list_of_values)
	a_cols = dict()
	sum = 0
	for a_val in a_list:
		a_cols[a_val[1][0]] = a_val[1][1]
	for b_val in b_list:
		if b_val[1][0] in a_cols.keys():
			sum += int(b_val[1][1]) * int(a_cols[b_val[1][0]])
	if sum > 0:
		mr.emit( (key[0], key[1], sum) )	

# Part 4
inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
