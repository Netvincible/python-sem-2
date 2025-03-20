def avg(lst,sum=0,index=0):
    if index==len(lst):
        return sum/(index)
    else:
        sum+=lst[index]
        return avg(lst,sum,index+1)

lst=[1,2,3,4]
print(avg(lst))
