#Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

for i in range(num1 + 1, num2):
    print(i)