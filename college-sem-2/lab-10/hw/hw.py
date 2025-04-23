with open("/home/netvincible/Documents/Python/college-sem-2/lab-10/hw/data.csv","r") as fd:
    content=fd.readline()
    content=fd.readline()
    i=1
    while(content):
        lst=content.split(",")
        fc=open(f"/home/netvincible/Documents/Python/college-sem-2/lab-10/hw/{i}.vcf","w")
        fc.write("BEGIN:VCARD\n")
        fc.write("VERSION:4.0\n")
        fc.write("FN:"+lst[0]+"\n")
        fc.write("TEL;TYPE=CELL:"+lst[1]+"\n")
        fc.write("EMAIL:"+lst[2])
        fc.write("END:VCARD\n")
        fc.close()
        i+=1
        content=fd.readline()
