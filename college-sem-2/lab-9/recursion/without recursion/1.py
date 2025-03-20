def check_prime(num):
    last=int(num**0.5)
    i=2
    while (num%i!=0 and i<=last):
        if i==last:
            return True
        i+=1
    else:
        return False

def prime_fact(num):
    domain=[x for x in range(2,int(num**0.5)+1)]
    it=0
    end=len(domain)
    while(it<end):
        if num%domain[it]==0:
            for i in domain:
                if i>domain[it] and i%domain[it]==0:
                    domain.remove(i)
                    end-=1
        else:
            domain.remove(domain[it])
            end-=1
            it-=1
        it+=1
            
    y=domain[0]
    temp=y
    while(num%(y*temp)==0):
        y=y*temp

        
    if check_prime(num/y):
        domain.append(int(num/y))

    return domain

# num=int(input("Enter a positive number: "))
ans=prime_fact(334)
print(ans)