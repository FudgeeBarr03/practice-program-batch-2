#Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers.
even_numbers = 0
for i in range(10):
    numbers = int(input("Enter a number: "))
    if numbers % 2 == 0:
        even_numbers += 1

print(f"There are a total of {even_numbers} even numbers.")