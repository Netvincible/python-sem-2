with open("/home/netvincible/Documents/Python/college-sem-2/lab-10/8/paragraph.txt","r") as fo:
    with open("/home/netvincible/Documents/Python/college-sem-2/lab-10/8/output.txt","w") as fw:
        line=fo.readline()
        while(line):
            line=line.split()
            for i in range(len(line)):
                if (line[i]=="an" or line[i]=="An" or line[i]=="a" or line[i]=="A" or line[i]=="the" or line[i]=="The"):
                    line[i]=" "
            line=" ".join(line)+"\n"
            fw.write(line)
            line=fo.readline()
