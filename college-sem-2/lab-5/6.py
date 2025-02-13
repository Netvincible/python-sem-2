def FtoC(lst):
	for i in range(len(lst)):
		lst[i]=(lst[i]-32)*9/5
	print(lst)

lst=[5,45,84,56,23]
FtoC(lst)
