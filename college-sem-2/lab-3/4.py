def removestring(string1,string2):
    if (string1.find(string2)>=0):
        string1=string1.replace(string2,"")
    print(string1)
string1=input("enter string 1: ")
string2=input("enter string 2: ")
removestring(string1,string2)