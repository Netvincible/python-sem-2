def fibonacci(n):
	a=0
	b=1
	c=0
	print("0,1",end=",")
	for i in range(n-2):
		c=a+b
		print(c,end=",")
		a=b
		b=c
	print()

fibonacci(8)
