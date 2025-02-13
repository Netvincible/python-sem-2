def stack(lst):
        x=1 
        while(x!=0):
                print("enter 0 to exit")
                print("enter 1 to append a value at start")
                print("enter 2 to remove a value at start")
                print("enter 3 to view the value at start") 
                print("enter 4 to view entire list")
                x=int(input("enter your value: "))
                if x==1:    
                        lst.insert(0,(int(input("enter value to insert: "))))
                elif x==2:  
                        if lst:   
                                lst.pop(0)
                elif x==3:  
                        if lst:   
                                print(lst[0])
                elif x==4:
                        print(lst)
                else:
                        pass
lst=[]    
stack(lst)



