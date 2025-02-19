def days(t1,t2):
	temp=t1[2]
	temp2=t2[2]

	if t1[1]>2:
		temp+=1            # if feb has passed then no need for that year in t1

	if (temp%4!=0):
		temp+=t1[2]%4

	if t2[1]<=2:		   # if feb has not passed then no need for that year in t2
		temp2-=1

	leaps=(temp2-temp+4)//4    # (last term - first term + common difference)//common differnce = no. of inclusive terms

	if (t2[2]//100 - t1[2]//100)>=1:	
		leaps-=( (t2[2]//100 - t1[2]//100)-(t2[2]//100 - t1[2]//100)//4 ) # centuries which are not factor of 400

	months=(1,-2,1,0,1,0,1,1,0,1,0,1)

	if t1[1]>t2[1]:
		mdays=-sum(months[(t2[1]-1):(t1[1]-1)])
	else:
		mdays=sum(months[(t1[1]-1):t2[1]-1])		
	
	days_between= t2[0]-t1[0] + (t2[1]-t1[1])*30 + (t2[2]-t1[2])*365+mdays+leaps

	print(leaps,mdays)
	return days_between

print(days((28,5,1600),(1,3,2000)))

