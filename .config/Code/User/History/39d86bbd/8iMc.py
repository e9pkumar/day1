def answer(num):
    #l=[]
    
    while num < 1000:
        l=[]
        for i in range (0,1000):
            if i%3 == 0:
                l.append(i)
            elif i%5 == 0:
                if i in l:
                    pass
                else:
                    l.append(i)
            elif i%15 == 0:
                if i in l:
                    pass
                else:
                    l.append(i)

        return(l)
        
        #return(sum(l))

num=999
result = answer(1000)
print(result)
