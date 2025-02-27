import random as r
def genrandom_inSet():
    st=set()
    st2=set()
    cnt=0

    while (len(st)<10):
        st.add(r.randint(15,45))

    print(st)
    
    for i in st:
        if i<30:
            cnt+=1
        elif i>35:
            st2.add(i)
    
    print(f"there are {cnt} values above 30 in set")
    
    st-=st2

    print(st)

genrandom_inSet()