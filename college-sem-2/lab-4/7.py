def fact(num):
	if (num==1 or num==0):
		return 1
	else:
		return num*fact(num-1)
		
def nCr(n,r):
	print("nCr=",fact(n)/(fact(n-r)*fact(r)))
def nPr(n,r):
	print("nPr=",fact(n)/fact(n-r))
nCr(5,3)
nPr(5,3)
