def substring(string1,string2):
    if (string1.find(string2)>=0 or string2.find(string1)>=0):
        print("TRUE")
    else:
        print("FALSE")
string1=input("enter string 1: ")
string2=input("enter string 2: ")
substring(string1,string2)