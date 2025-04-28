class date:
    def __init__(self,lst=[1,1,1]):
        self.lst=lst
    def __eq__(self,d2):
        if self.lst==d2.lst:
            return True
        else:
            return False
dt=date([1,4,2025])
dt2=date([28,4,2025])
dt3=date([1,4,2025])
print(dt==dt2)
print(dt==dt3)

            