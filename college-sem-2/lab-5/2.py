import random as r
def searching():
	lst=[]
	for i in range(0,20):
		lst.insert(i,r.randint(1,20))
	print(lst)
	x=int(input("enter num: "))
	indices = [i for i, val in enumerate(lst) if val ==x]
	print("Indices of", x, ":", indices)
searching()
