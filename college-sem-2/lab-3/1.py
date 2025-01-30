def vowelcount(string):
    count=0
    count+=string.count("a")
    count+=string.count("e")
    count+=string.count("i")
    count+=string.count("o")
    count+=string.count("u")
    print(count)
string=input("enter string: ")
vowelcount(string)