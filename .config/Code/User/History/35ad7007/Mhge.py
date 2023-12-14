def solver(factors, start, end):
    sum1=0
    numbers=range(start,end)
    #l=[]
    for j in (factors):
            
        for i in numbers:
            if (i%j==0): 
                sum1+=i
            i += 1

        return(sum1)
    
result=solver([2, 3, 5, 7, 11], 34567, 1234567) 
print(result)


'''def MultiplesSum(multiple, end, start=1):
    mSum = 0
    naturals = range(start, end)
    offset = -start 
    if start == 0:
      raise ZeroDivisionError('Cannot start with the number 0')
    for num in multiple:
      for i in naturals:
        if i % num == 0 and naturals[i+offset] != 0:
          # print mSum,"+", i,"=",i+mSum
          mSum += i
          naturals[i+offset] = 0
        i += 1
    return mSum

problem1 = MultiplesSum([3,5,2], 16)
print problem1'''