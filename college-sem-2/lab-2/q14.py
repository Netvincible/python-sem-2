a = int(input("enter the marks of first subject:"))
b = int(input("enter the marks of second subject:"))
c = int(input("enter the marks of third subject:"))
sum = a+b+c

def check(a,b,c,sum):
    average = sum/3
    if(a<=39 or b<=39 or c<=39):
        print("fail")
    elif(39<average<45):
        print("P")
    elif(44<average<50):
        print("C")
    elif(49<average<55):
        print("B")
    elif(54<average<60):
        print("B+")
    elif(59<average<70):
        print("A")
    elif(69<average<80):
        print("A+")
    else:
        print("O")
        
check(a,b,c,sum)
    