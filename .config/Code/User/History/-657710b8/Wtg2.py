def solver(factors, start, end):
    
    l=[]
    #for j in (factors):
    for i in range(start,end):
        for j in factors:
            if (i%j==0):
                if i not in l:
                    l.append(i)
            else:
                pass

    return(sum(l))
    
result=solver([4,7,11], 8912, 40512)
print(result)