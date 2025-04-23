palindrome=lambda s: True if s== s[::-1] else False
lst=["madam","Python","malayalam",12321]
ans=list(filter(palindrome,map(str,lst)))
print(ans)

