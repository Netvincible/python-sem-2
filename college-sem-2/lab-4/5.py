def pytha_trip(c):
	i=1						# for pythagorean triplet a,b,c where a<b<c,i is the iterator for a, j is the iterator for c and value of b should be an integer
	while (2*i*i<c*c):                              # iterator i for a can never be greater than (c^2)/2 as max value of a is less than b
		for j in range(i+1,c+1):		# now iterator j for c, max value is c and min val is i+1 as we have fixed value of a which is iterator i
			b=(j**2 - i**2)**0.5
			if(b//1==b and i<b):            # using condition a<b and checking if b is integer or not, you can also use type(b)==int
				print(i,int(b),j)
		i+=1

pytha_trip(30)
