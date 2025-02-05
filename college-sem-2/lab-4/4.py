def isprime(num):
	i=2
	while (i*i<=num):
		if (num%i==0):
			print("number is not prime")
			break
		i+=1
	else:
		print("number is prime")

def isperfect(num):
	sum=1
	check=0
	i=2
	while (check!=i and i<num):
		if(num%i==0):
			check=num//i
			sum=sum+i+num//i
		i+=1
	if (sum==num):
		print("number is perfect")
	else:
		print("number is not perfect")

def isarmstrong(num):
	string=str(num)
	sum=0
	for ch in string:
		sum+=int(ch)**len(string)
	if (sum==num):
		print("number is armstrong")
	else:
		print("number is not armstrong")

def ispalindrome(num):
	num=str(num)
	for i in range(0,len(num)//2):
		if (num[i]!=num[-1-i]):
			print("number is not palindrome")
			break
	else:
		print("number is palindrome")

def isautomorphic(num):
	if((num**2)%10**len(str(num))==num):
		print("number is automorphic")
	else:
		print("number is not automorphic")



num=int(input("enter number: "))
isprime(num)
isperfect(num)
isarmstrong(num)
ispalindrome(num)
isautomorphic(num)
