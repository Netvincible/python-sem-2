def sum_avg(a,b,c,d,e):
    total=sum(locals().values())
    avg=total/5
    return total,avg
    

print(*sum_avg(1,2,3,4,5))