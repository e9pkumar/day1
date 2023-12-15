def evenify(input_numbers):
    even_numbers = []
    for i in input_numbers:
        if i % 2 == 0:
            even_numbers.append(i)
    return even_numbers

def max_number(items):
    max_number = 0
    maximum = items[0]

    for i in items:
        if i > maximum:
            maximum = i
            max_number = i

    return max_number



def sautee(sentence):
    string1= sentence.split()
    for i in string1:
        string1=string1[::-1]
        string2=" ".join(string1)
        return string2


# 4.flambe(sentence): returns a new list with the words sorted by their length.

def flamebe(sentence):

    string1 = sentence.split()
    string2= sorted(string1,key=len)
    return string2


from datetime import datetime

def poach(dt):
    if not isinstance(dt, datetime):
        raise ValueError("Input must be a datetime object.")
    return dt.year % 4 == 0 and (dt.year % 100 != 0 or dt.year % 400 == 0)


import math  
def heron(a,b,c):
    s = ((a+b+c)/2)
    area = math.sqrt((s * (s - a) * (s - b) * (s - c)))

    return area




# heron(a, b, c): return the area of a triangle given the lengths of its three sides (Heron's formula).
# 5. s = (a + b + c) / 2
#    area = √(s * (s - a) * (s - b) * (s - c))




if __name__ == "__main__":
    # 1: Evenify
    n = int(input("Enter the number of items you want: "))
    l = [int(input()) for _ in range(n)]
    print("Original list:", l)
    result = evenify(l)
    print("Even numbers from the list:", result)

    # 2: Max Number
    n = int(input("Enter number of items in the list: "))
    items = [int(input()) for _ in range(n)]
    print("List:", items)
    print("Maximum number:", max_number(items))


    # 3:Take a sentence and return the sentence with the words in reverse order
    sentence=input("Enter any sentence:")
    print(sautee(sentence))

    # 4:Returns a new list with the words sorted by their length.
    sentence = input("Enter the sentence:")
    print(flamebe(sentence))

    # 5:Leap year or not
    try:
        input_date = input("Enter a date (YYYY): ")
        date = datetime.strptime(input_date, "%Y")
        result = poach(date)
        print(f"The year {date.year} {'is' if result else 'is not'} a leap year.")
    except ValueError as e:
        print(f"Error: {e}")

    

    # 6: Heron Formula
    a=int(input("Enter any number:"))
    b=int(input("Enter any number:"))
    c=int(input("Enter any number:"))

    print(heron(a,b,c))

    


    