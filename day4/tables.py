def table(num):
   lst = [num*i for i in range(1,21)]
   return(lst)

if __name__=="__main_":
   num=int(input("Enter any number"))
   print(table(num))