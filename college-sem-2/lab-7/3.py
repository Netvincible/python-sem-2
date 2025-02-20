def min_max(rec):
	max_val=max(rec.values())
	min_val=min(rec.values())
	print(list(rec.keys())[list(rec.values()).index(max_val)],"has the maximum salary",max_val)
	print(list(rec.keys())[list(rec.values()).index(min_val)],"has the minimum salary",min_val)

rec={(1,4012):1000,(2,2023):500,(3,1065):20000}
min_max(rec)
