a="hello"
while(type(a)!=int):
    try:
        a=int(input("enter integer "))
    except:
        print("try again")
    