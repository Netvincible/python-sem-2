import random as r
def genran():
	lst=[]
	for i in range(50):
		lst.append(r.randint(1,30))
	print(lst)
	for i in lst:
		for j in range(lst.count(i)-1):
			lst.remove(i)
	print(lst)
#genran()


def genran2():
	lst=[]
	mp={}
	for i in range(50):
		x=r.randint(1,2)
		lst.append(x)
		mp[x]=0
	print(lst)
	last=len(lst)
	iter=0
	while iter<last:
		mp[lst[iter]]+=1
		if mp[lst[iter]]>1:
			lst.pop(iter)
			last-=1
			iter-=1
		iter+=1
			
	print(lst,"\n",mp)

genran2()
