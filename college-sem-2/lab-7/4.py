def freq():
	string=input("enter string: ")
	hash={}
	for i in string:
		hash[i]=0
	for i in string:
		hash[i]+=1
	print(hash)
freq()
