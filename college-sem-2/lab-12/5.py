class time:
    def __init__(self,hour=0,minute=0,second=0):
        self.hour=hour
        self.minute=minute
        self.second=second

    def __sub__(self,t2):
        difference=self.hour*60*60+self.minute*60+self.second - (t2.hour*3600+t2.minute*60+t2.second)
        ans=time()
        ans.hour=difference//3600
        difference-=ans.hour*3600
        ans.minute=difference//60
        difference-=ans.minute*60
        ans.second=difference
        return ans
    def __add__(self,t2):
        add=self.hour*60*60+self.minute*60+self.second + (t2.hour*3600+t2.minute*60+t2.second)
        ans=time()
        ans.hour=add//3600
        add-=ans.hour*3600
        ans.minute=add//60
        add-=ans.minute*60
        ans.second=add
        return ans
    def __str__(self):
        return f"{self.hour}:{self.minute}:{self.second}"
t1=time(10,10,10)
t2=time(4,20,20)
print(t1+t2)
print(t1-t2)
