def isline():
    x1,y1=input("enter coordinates of point 1:").split()
    x2,y2=input("enter coordinates of point 2:").split()
    x3,y3=input("enter coordinates of point 3:").split()
    x1,y1=int(x1),int(y1)
    x2,y2=int(x2),int(y2)
    x3,y3=int(x3),int(y3)
    if (y1*(x2-x3)+y2*(x3-x1)+y3*(x1-x2))==0:
        print("all three points are in line")
    else:
        print("all three points are not in line")
isline()