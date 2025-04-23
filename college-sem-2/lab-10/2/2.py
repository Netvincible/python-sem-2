dict={}
fr=open("/home/netvincible/Documents/Python/college-sem-2/lab-10/2/marksheet.csv","r")
lst=fr.readline().split(',')
l1=fr.readline().split(',')
flag=0
while l1!=['']:
    for i in lst:
        if flag==0:
            dict[i]=[l1[lst.index(i)]]
        else:
            dict[i]+=[l1[lst.index(i)]]
    flag+=1
    l1=fr.readline().split(',')

fr.close

print(dict)
    
