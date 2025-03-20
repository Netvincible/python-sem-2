
l=[]
def prime_fact(num):
    factors=0
    for x in range(2,num): 
        if num%x==0:
            prime_fact(x)
            factors+=1
    if factors==0:
        l.append(num)

prime_fact(344)
l=set(l)
print(l)