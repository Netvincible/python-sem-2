l=[]

def prime_fact(num):
    x=int(num**0.5)
    if x<=1:
        return num
    while(num%x!=0):
        x-=1
        if x<=2:
            return num
    else:
        a=prime_fact(x)
        if a!=None:
            l.append(a)
        a=prime_fact(num/x)
        if a!=None:
            l.append(a)
            
prime_fact(4284)
print(l)