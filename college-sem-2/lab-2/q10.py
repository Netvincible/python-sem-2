def larger_ar_peri():
    l=int(input("enter lenght:"))
    b=int(input("enter breadth:"))
    if(l*b>2*(l+b)):
        print("area is greater than perimeter")
    else:
        print("area is equal to or less than perimeter")
larger_ar_peri()