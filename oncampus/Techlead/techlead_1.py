# 1. Write a program to find the Factorial of a given number using Recursion.

def fact(n):
    if n in (0, 1):
        return 1
    
    if n >= 2:
        return n * fact(n - 1)


num = int(input("Enter number to get factorial: "))

if num < 0:
    print("Enter valid positive number")
else:
    print(f"Factorial of {num} : {fact(num)}")