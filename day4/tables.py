def multiplication_table(num):
    print(f"Multiplication Table for {num}\n")
    for i in range(1, 21):
        result = num * i
        print(f"{num:2} x {i:2} = {result:4}")

# Program 4: Multiplication Table
        
if __name__ == "__main__":
    num = int(input("Enter the number: "))
    multiplication_table(num)
