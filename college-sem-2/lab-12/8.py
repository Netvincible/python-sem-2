class String:
    def __init__(self,val=""):
        self.val=val
    
    def __iadd__(self,s2):
        self.val+=s2.val
        return self
    
    def toLower(self):                # we can do it by using self.val.lower() but then there's no point of making this function
        s=String()
        for i in self.val:
            if ord(i)>=65 and ord(i)<97:
                s.val+=chr(ord(i)+32)
            else:
                s.val+=i
        return s
    
    def toUpper(self):                # we can do it by using self.val.uppper() but then there's no point of making this function
        s=String()
        for i in self.val:
            if ord(i)>=97 and ord(i)<123:
                s.val+=char(ord(i)-32)
            else:
                s.val+=i    
        return s
    def __str__(self):
        return self.val

st=String("Hi my Name is Netra")
st+=String(" Sorathiya")
print(st)
print(st.toLower())