#I would like all of you to run your code for the following args.

#1. Send me the answer for solver([2, 3, 5, 7, 11], 34567, 1234567)
#2. Ensure that your program runs in < 1 minute.
#3. Submit the updated code, if applicable, to github.
#4. Your solution must be uniquely yours. We are running sophisticated algorithms that have identified several submissions to be meaningfully identical.




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