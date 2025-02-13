import random as r
def fun():
	lst1=[]
	lst2=[]

	for i in range(10):
		lst1.append(r.randint(1,30))
		lst2.append(r.randint(1,30))
	
	lst3= [x for x in lst1 if x not in lst2 ]
	print(lst1)
	print(lst2)
	print(lst3)

fun()
