def solver(factors, start, end):
    
    l=[]
    #for j in (factors):
    for i in range(start,end+1):
        for j in factors:
            if (i%j==0):
                if i not in l:
                    l.append(i)
                j=j+1
            else:
                pass

    return(sum(l))
    
result=solver([2, 3, 5, 7, 11], 34567, 1234567) 
print(result)