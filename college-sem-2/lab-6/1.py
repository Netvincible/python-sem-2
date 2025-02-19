def boy_girl():
	b=0
	g=0
	lst=[("hitarth",),("Nisarg",),("Prince",),"Yashvi","Yashashvi","Neeti"]
	for ele in lst:
		if isinstance(ele,tuple):
			b+=1
		elif ( isinstance(ele,str) ):
			g+=1
	print("boys:",b,"girls:",g)
boy_girl()
