def count_lower_upper(Str):
    lower_case=0
    upper_case=0
    for ch in Str:
        if ch.islower():
            lower_case+=1
        elif ch.isupper():
            upper_case+=1
    res={"lower_case":lower_case,"upper_case":upper_case}
    return res

Str="Hi Hello My Name is Netra."
print(count_lower_upper(Str))