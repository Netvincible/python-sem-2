def frequency(string):
    freq={}
    strlist=sorted(string.split())
    for i in strlist:
        freq[i]=0
    for i in strlist:
        freq[i]+=1
    
    return freq
    

print(frequency("hi hello my name is netra. hello world"))