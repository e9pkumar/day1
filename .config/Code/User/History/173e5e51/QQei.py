def add(a,b):
    total=0
    a=4212
    b=18912512
    for i in range (a,b+1):
        total=total+i
        a=a+i
        a+=1

result=add(a,b)
print(result)