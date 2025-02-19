def rm_empty_tup(lst):
	for ele in lst:
		if not ele:
			lst.remove(ele)
	return lst

lst=[(),(2,3,5),(),(3,1,534,56),()]
print(lst)
lst=rm_empty_tup(lst)
print(lst)
