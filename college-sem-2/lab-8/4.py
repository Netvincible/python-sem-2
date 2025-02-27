def seperation(st):
    stA={x for x in st if x[0]=='A'}
    stB=st-stA
    print(f"{st}\n{stA}\n{stB}")

st={"Abhinav","Bhautik","Aaditya","Bhavin","Abhisekh","Bhavik"}
seperation(st)