"""Write a Python program to calculate the sum of three numbers. 
If all three numbers are equal, return three times their sum."""

def add_three(a,b,c):
    sum = a + b + c
    if a == b and b==c:
        sum = sum*3
    return sum

a = int(input("ENTER THE VALUE OF a: ")) 
b = int(input("ENTER THE VALUE OF b: ") )
c =  int(input("ENTER THE VALUE OF c: "))

print(add_three(a,b,c))



