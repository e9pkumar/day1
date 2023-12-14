#def solver(start, end, even, odd):
    
def solver(start, end):
    #number=range(start,end)
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
  
start=10
end=100
f1=list(solver(start,end))
print (f1)
