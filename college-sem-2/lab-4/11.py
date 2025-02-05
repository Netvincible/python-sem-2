def fact(num):   
        if (num==1 or num==0):
                return 1
        else:
                return num*fact(num-1)

def sin(x):
	ans=0
	for i in range(10):
		ans=ans + ((-1)**i) * ((x**(2*i+1))/fact(2*i+1))
	else:
		return ans
print(sin(3.14))

