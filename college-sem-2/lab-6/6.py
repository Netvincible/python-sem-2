def replace_tuple_val(tup,i,val):
	lst=list(tup)
	lst[i]=val
	tup=tuple(lst)
	return tup
	
tup=(10,9,8,7,6,5,4,3,2,1)
tup=replace_tuple_val(tup,4,12)
print(tup)
