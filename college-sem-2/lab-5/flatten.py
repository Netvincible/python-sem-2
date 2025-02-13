def flatten(lst):
    for i in lst:
        if type(i)==list:
            for j in i:
                lst.insert(lst.index(i),j)
            lst.pop(lst.index(i))
    return lst
