def sanitize(lst,index=0):
    if index==len(lst):
        return lst
    else:
        if lst[index]<0:
            lst[index]=0
        return sanitize(lst,index+1)

lst=[-5,56,58,-548,3,-6]
print(sanitize(lst))