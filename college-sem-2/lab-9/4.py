def sum_avg(*args):
    
    total=sum(args)
    avg=total/len(args)
    return total,avg
    

print(*sum_avg(1,2,3,4,5))