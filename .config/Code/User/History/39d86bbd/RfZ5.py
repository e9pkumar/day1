l=[]
def answer(num):
    
    
    while num < 1000:
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
        
print(sum(l))


            


