l=[]
def binary(num):
    if num==0:
        return l.reverse()
    else:
        l.append(num%2)
        binary(num//2)
        return l
print(binary(23))
# print l
    