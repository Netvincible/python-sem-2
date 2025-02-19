import random as r
def square_of_list():
	lst=[]
	for i in range(10):
		lst.append(r.randint(1,20))
	LS=[x**2 for x in lst]
	print(lst)
	print(LS)

square_of_list()
