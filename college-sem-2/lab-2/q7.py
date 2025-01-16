def isleap():
    a=int(input("enter year: "))
    if(a%4==0):
        if(a%100!=0 or a%400==0):
            print("leap year")
        else:
            print("not leap year")
    else:
        print("not leap year")
isleap()