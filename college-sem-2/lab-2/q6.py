def digit():
    a=int(input("enter a number: "))
    count=0
    if (a<0):
        a=-a
    while(a!=0):
        a=a//10
        count+=1
    print(count,"digits")
digit()