def ls3():
    a=int(input("enter a value:"))
    b=int(input("enter another value:"))
    c=int(input("enter another value:"))

    if (a>b):
        largest=a
        smallest=b
    else:
        largest=b
        smallest=a
        
    if (largest<c):
        largest=c
    if (smallest>c):
        smallest=c

    if (smallest==largest):
        print("all numbers are equal",largest)
    else:
        print("largest:",largest,"smallest:",smallest)
ls3()
