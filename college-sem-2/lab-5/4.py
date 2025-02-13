import random as r
def pos_neg():
	lst=[]
	for i in range(30):
		lst.append(r.randint(-50,50))
	lst1=[]
	lst2=[]
	for i in lst:
		if i>0:
			lst1.append(i)
		if i<0:
			lst2.append(i)
	print(lst1,"\n",lst2)
pos_neg()
