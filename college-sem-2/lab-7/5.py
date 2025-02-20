def bill(dict1,dict2):
	total=0
	for k,v in dict2.items():
		total+=v*dict1[k]
	return total

dict1={"banana":10,"apple":20,"orange":30,"pineapple":25,"kiwi":40,"dragon fruit":50}
dict2={"apple":2,"orange":3,"kiwi":1,"dragon fruit":1}
print("Your Total Bill is Rs.",bill(dict1,dict2))
