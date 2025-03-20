def exp(a,b):
    
    if b==0:
        return 1
    else:
        return a*exp(a,b-1)

print(exp(a=2,b=10))
    
    