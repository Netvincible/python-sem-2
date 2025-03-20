def create_array(a,b,c,n):
    lsc=[]
    for i in range(c):
        lsc.append(n)
    lsb=[lsc]*b
    lsa=[lsb]*a
    return lsa

print(create_array(4,3,2,1))