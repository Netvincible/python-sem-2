def con_dict(*dictionaries):

	new_dict={}
	for x in dictionaries:                 #dictionaries is tuple of arguments passed, here it is tuple of dictionries
		new_dict.update(x)
#	new_dict.update(x for x in dictionaries)  #ValueError: dictionary update sequence element #0 has length 3; 2 is required
	print(new_dict)
	

dict1={"name":"netra","branch":"cs","roll":62}
dict2={"sub":"eng","marks":63,"status":"pass"}
dict3={}

"""
dict1,dict2,dict3={},{},{}
for j in range(3):
	key=input("enter string key: ")
	dict1[key]=input("enter value: ")

for j in range(3):
	key=input("enter string key: ")
	dict2[key]=input("enter value: ")

for j in range(3):
	key=input("enter string key: ")
	dict3[key]=input("enter value: ")
"""

con_dict(dict1,dict2,dict3)
