#def evenify(input_numbers):

def get_list():
    n = int(input("Enter the number of items you want:"))
    l = []
    for i in range(n):
        n1=int(input())
        l.append(n1)
    print(l)
    
def evenify(get_list):
    input_numbers = []
    for i in get_list:
        if i % 2 == 0:
            input_numbers.append(i)

        else:
            pass

if __name__ == "__main__" :
    print(evenify(input_numbers(get_list)))

# 2. foo_max(items): find and return the maximum element in the list (items); you may not use the built-in max() function.
    
def foo_max(items):
    items = [2,8,9,6]
    max_number= 0
    maximum = items[0]
    for i in items :
        if i>maximum:
           max_number += i
        else:
            pass
    return(max_number)
#if __name__ == "__main__":
    #print(foo_max(items=[2,8,9,6]))


# 3. sautee(sentence): take a sentence and return the sentence with the words in reverse order.

def sautee(sentence):
   
    string1 = sentence.split()
    

    for each in string1 :
        each = each[::-1]
        string1.append(each)
    string2 = "".join(string1)

    return string2
    
if __name__ == "__main__" :
    sentence = input("Enter any sentence:")
    print(sautee(sentence))


    
# 4.flambe(sentence): returns a new list with the words sorted by their length.
