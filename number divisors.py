"""Write a Python program to ask the user for a number and print all its divisors"""

number = int(input())

for i in range(1,number+1):
    if number % i == 0:
        print(i)