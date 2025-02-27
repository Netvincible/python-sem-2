def seperation(st):
    st1={x for x in st if x[0]=='A'}
    st2=st-st1
    print(f"{st}\n{st1}\n{st2}")

st={"Abhinav","Bhautik","Aaditya","Bhavin","Abhisekh","Bhavik"}
seperation(st)