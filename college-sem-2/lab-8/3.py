def setoperation():
    st=set()
    for i in range(5):
        st.add(input("Enter a unique name: "))
    
    print(st)

    old_name=input("enter name to modify : ")
    if old_name in st:
        new_name=input("enter new name: ")
        st.remove(old_name)
        st.add(new_name)

    print(st)
    
    for i in range(2):
        print(f"{st.pop()} is removed")

    print(st)

setoperation()