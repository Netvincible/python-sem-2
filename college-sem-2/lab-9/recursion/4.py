
def reverse(lst,index=0):
    if index==len(lst):
        return lst
    
    lst[index]=int(str(lst[index])[::-1])
    index+=1
    return reverse(lst,index)

lst=[12,34,53,67]
print(reverse(lst))
