def UppercaseSet(lst):
    st={x.upper() for x in lst if (type(x)==str and x.isalnum())}
    return st
lst=["hello","--=!#","4riour","hi5ve","PDEU","pdeu"]
print(UppercaseSet(lst))
