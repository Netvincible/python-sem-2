def min_max(rec):
	for k,v in rec.items():
		for i in v:
			min_sal=min(i[1] for i in v)
			max_sal=max(i[1] for i in v)
		print(f"{k} has min salary:{min_sal} and max salary:{max_sal}")

rec={"CSE":((1,2000),(2,3000),(3,1000)),"EC":((1,500),(2,5000),(3,50000)),"ICT":((1,700),(2,500))}
min_max(rec)
