def stack(lst):
	x=1
	while(x!=0):
		print("enter 0 to exit")
		print("enter 1 to append a value")
		print("enter 2 to remove a value")
		print("enter 3 to view the value")
		print("enter 4 to view entire list")
		x=int(input("enter your value: "))
		if x==1:
			lst.append(int(input("enter value to append: ")))
		elif x==2:
			if lst:
				lst.pop()
		elif x==3:
			if lst:
				print(lst[-1])
		elif x==4:
			print(lst)
		else:
			pass	
lst=[]
stack(lst)
