def function(lst):
	LS=[x for x in lst if x.find("a")>-1]
	print(LS)
lst=[]
for i in range(5):
	lst.append(input("enter string: "))
function(lst)
