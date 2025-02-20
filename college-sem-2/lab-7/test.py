c=10
dict={1:c,2:20,3:30}
print(dict)
print(dict.items())
a=list(dict.items())
print(a)
print(type(a[0]))

dict[1]=100
print(c,dict)
