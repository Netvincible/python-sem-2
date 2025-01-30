def isline():
    x1,y1=map(int,input("enter coordinates of point 1:").split())
    x2,y2=map(int,input("enter coordinates of point 2:").split())
    x3,y3=map(int,input("enter coordinates of point 3:").split())
    if (y1*(x2-x3)+y2*(x3-x1)+y3*(x1-x2))==0:
        print("all three points are in line")
    else:
        print("all three points are not in line")
isline()