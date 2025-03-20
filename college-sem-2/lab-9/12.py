def fun():
	print("fun")
def disp():
	print("disp")
def msg():
	print("msg")

lst=[fun,disp,msg]
for i in lst:
	i()
