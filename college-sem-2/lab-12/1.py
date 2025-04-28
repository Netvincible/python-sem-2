class complex:
    def __init__(self,real=0,imag=0):
        self.x=real
        self.y=imag
    def __add__(self,z2):
        ans=complex(self.x+z2.x,self.y+z2.y)
        return ans
    def __sub__(self,z2):
        ans=complex(self.x-z2.x,self.y-z2.y)
        return ans
    def __mul__(self,z2):
        ans=complex(self.x*z2.x - self.y*z2.y,self.x*z2.y+self.y*z2.x)
        return ans
    def __truediv__(self,z2):
        ans=complex((self.x*z2.x-self.y*z2.y)/(z2.x**2+z2.y**2),(self.y*z2.x-self.x*z2.y)/(z2.x**2+z2.y**2))
        return ans
    def __str__(self):
        return (f"{self.x}+{self.y}i")
z1=complex(3,5)
z2=complex(6,8)
add=z1+z2
print(add)
print(z1-z2)
print(z1*z2)
print(z1/z2)
    