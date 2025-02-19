def delete_tuple_val(tup,i):
	lst=list(tup)
	lst.pop(i)
	tup=tuple(lst)
	return tup
	
tup=(10,9,8,7,6,5,4,3,2,1)
tup=delete_tuple_val(tup,4)
print(tup)
