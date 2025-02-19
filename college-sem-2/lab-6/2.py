def list_sep(lst):
	roll=[]
	name=[]
	age=[]


	for l in lst:
		roll.append(l[0])
		name.append(l[1])
		age.append(l[2])
	print(roll)
	print(name)
	print(age)

register=[(3,"shyam",17),(52,"hitarth",18),(57,"het",18),(58,"prince",19),(62,"netra",18),(65,"nisarg",18)]
list_sep(register)
