def hrs():
	print("midnight")
	for i in range(1,24):
		if (i<12):
			print(i,": 00 AM")
		elif(i==12):
			print("noon")
		elif(i>12):
			print(i-12,": 00 PM")
hrs()
