def count_alpha_num(string):
	calpha,cdigit=0,0
	for ch in string:
		if ch.isalpha():
			calpha+=1
		elif ch.isdigit():
			cdigit+=1
	print("number of digits:",cdigit,"number of alphabets:",calpha)
string=input("enter string: ")
count_alpha_num(string)
