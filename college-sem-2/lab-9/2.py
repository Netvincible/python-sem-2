def compute(n):
    ns=str(n)
    return (int(ns)+int(ns*2)+int(ns*3) + int(ns*4))

for i in range(4,8):
    print(i,compute(i))