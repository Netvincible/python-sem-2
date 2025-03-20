lst=["faculty","facutlyA","faculty ","faculty AB","faculty ABCD"]
fun=lambda s: True if len(s)>8 else False
ans=list(filter(fun,lst))
print(ans)
