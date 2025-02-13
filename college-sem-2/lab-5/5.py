def upper_string(lst):
	for i in range(len(lst)):
		lst[i]=lst[i].upper()
	print(lst)
lst=[]

for i in range(5):
	lst.append(input("enter the string: "))

upper_string(lst)
