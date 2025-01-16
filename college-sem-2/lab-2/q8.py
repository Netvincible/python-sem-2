def isvalidtriangle():
    a=int(input("enter angle A:"))
    b=int(input("enter angle B:"))
    c=int(input("enter angle C:"))
    if (a+b+c==180):
        print("triangle is valid")
    else:
        print("invalid triangle")
isvalidtriangle()