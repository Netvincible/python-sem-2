class weather:
    def __init__(self,*args):
        self.lst=[]
        for i in args:
            self.lst.append(i)
    def __contains__(self,parameter):
        return parameter in self.lst
day1=weather("moisture","aqi","sky")
print("humidity" in day1)
print("moisture" in day1)
