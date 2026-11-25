"""Write a Python program that accepts an integer n and calculates the value of n + nn + nnn."""

result = lambda n: int(str(n)) + int(str(n)*2) + int(str(n)*3)

n = int(input())

print(result(n))

#result = lambda n: n + (n *n) + (n*n*n)
#n = int(input())
#print(result(n))
