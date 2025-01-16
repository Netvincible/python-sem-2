def ls2():
    a=int(input("enter a value:"))
    b=int(input("enter another value:"))
    if (a<b):
        print(a,"<",b)
    elif (a>b):
        print(a,">",b)
    else:
        print(a,"=",b)

ls2()