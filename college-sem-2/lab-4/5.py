def pytha_trip(num):
	i=1
	while (2*i*i<num*num):
		for j in range(i+1,num+1):
			a=(j**2 - i**2)**0.5
			if(a//1==a and i<a):
				print(i,int(a),j)
		i+=1

pytha_trip(30)
