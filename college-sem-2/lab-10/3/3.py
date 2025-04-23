dict={"NAME":"","PHONE":0}
name=input("enter name: ")
phone=input("enter number: ")
with open("1.vcf","w") as f:
    f.write("BEGIN:VCARD\n")
    f.write("VERSION:4.0\n")
    f.write("FN:"+name+"\n")
    f.write("TEL;TYPE=CELL:"+phone+"\n")
    f.write("END:VCARD\n")