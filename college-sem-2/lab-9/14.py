import random as r
l=[]
while (len(l)<=10):
	l.append(r.randint(-15,15))
lst=list(map(lambda x:x*x,l))
print(l)
print(lst)
