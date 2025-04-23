f=open("marksheet.csv","a+")
rlno=input("enter roll no[enter to end]: ")
while rlno:
    nm,cp,math,che=input("enter name, cp, math, che separated by space: ").split(",")
    f.write(rlno+','+nm+','+cp+','+math+','+che+'\n')
    rlno=input("enter roll no[enter to end]: ")
f.close()

f=open("marksheet.csv","r+")
content=f.read()
print(content)

