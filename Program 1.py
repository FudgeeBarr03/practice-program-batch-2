#Prog01: Create a program that ask user to input 2 numbers. Print the smaller number.
num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))

if num_1 < num_2:
    print(f"{num_1} is the smaller number")
else:
    print(f"{num_2} is the smaller number")