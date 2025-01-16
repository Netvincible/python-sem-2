from numpy import sqrt 
def incircle():
    x1,y1=input("enter coordinates of point 1:").split()
    x1,y1=int(x1),int(y1)

    x,y=input("enter coordinates of centre:").split()
    x,y=int(x),int(y)
    r=int(input("enter the radius of circle:"))
    if (sqrt((x-x1)**2 + (y-y1)**2)>r):
        print("point is outside of the circle")
    elif (sqrt((x-x1)**2 + (y-y1)**2)<r):
        print("point is inside the circle")
    else:
        print("point is on the circle")
incircle()