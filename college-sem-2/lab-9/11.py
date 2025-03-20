def create_list(lst1,lst2):
    result=[]
    for i in set(lst1):
        if lst2.count(i):
            result.append(i)
    return result

lst1=[6,4,3,4,6,4,82,4,10]
lst2=[1,4,6,9,4,7,3,3,34,6,2]
print(create_list(lst1,lst2))