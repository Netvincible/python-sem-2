import random as r
import mymod

lodd=[]
for i in range(5):
    lodd.append(2*r.randint(1,5)+1)
print(f"list of odd int: {lodd}")

leven=[]
for i in range(4):
    leven.append(2*r.randint(1,5))
print(f"list of even int: {leven}")

lodd[2]=leven
print("replacing 3rd element of odd list with even list:",lodd)

print("after flatening the odd list is:",mymod.flatten(lodd))

lodd.sort()
print("after sorting list is: ",lodd)