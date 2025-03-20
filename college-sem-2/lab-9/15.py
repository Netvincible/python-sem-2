palindrome=lambda s: True if s[ 0:int(len(s)/2) ]==s[:int(len(s)/2):-1] else False
lst=["madam","Python","malayalam",12321]
ans=list(filter(palindrome,map(str,lst)))
print(ans)

