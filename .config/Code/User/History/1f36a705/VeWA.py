
def answer(num):
    a,b=0,1
    while a <= num:
        yield a
        a,b=b,a+b
 
 
num=4000000           
c=tuple(answer(num))
print(c)
even_num = sum(tuple(filter(lambda x : x%2==0,c)))
print(even_num)