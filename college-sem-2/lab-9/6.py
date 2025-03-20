def PowersOfx(n):
    lst=[(x,x**2,x**3) for x in range(1,n+1)]
    return lst

print(PowersOfx(5))