class matrix:
    def __init__(self,mat=[]):
        self.mat=mat
        if (len(mat)==0):
            self.n,self.m=map(int,input("enter nxm for ").split("x"))
            for i in range(self.n):
                mat.append([])
                for j in range(self.m):
                    mat[i].append(int(input("enter ["+str(i+1)+"]"+"["+str(j+1)+"]: " )))
        else:
            self.n=len(mat)
            self.m=len(mat[0])

    def __add__(self,mat2):
        if(self.n==mat2.n and self.m==mat2.m):
            ans=[]
            for i in range(self.n):
                lst=[]
                for j in range(self.m):
                    lst.append(self.mat[i][j]+mat2.mat[i][j])
                ans.append(lst)
            ans=matrix(ans)
            return ans
        else:
            return "matrix are not of same order."

    def __mul__(self,mat2):
        if(self.m==mat2.n):
            ans=[]
            for i in range(self.n):
                ans.append([])
                for j in range(mat2.m):
                    sum=0
                    for k in range(self.m):
                        sum+=self.mat[i][k]*mat2.mat[k][j]
                    ans[i].append(sum)
            ans=matrix(ans)
            return ans
        else:
            return "invalid matrices"
    def transpose(self):
        ans=[]
        for i in range(self.m):
            ans.append([])
        for i in range(self.n):
            for j in range(self.m):
                ans[j].append(self.mat[i][j])
        ans=matrix(ans)
        return ans
    def printm(self):
        for i in range(self.n):
            for j in range(self.m):
                print(self.mat[i][j],end=" ")
            print()
m1=matrix([[1,2,3],[4,5,6],[7,8,9]])
m2=matrix()
(m1+m2).printm()
(m1*m2).printm()
(m1.transpose()).printm()
