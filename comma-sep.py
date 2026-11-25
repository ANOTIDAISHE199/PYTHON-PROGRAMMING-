"""Write a Python program that accepts comma-separated numbers from the user and creates a 
list and a tuple containing those numbers.
"""


comma_sep = input("Enter comma-separated numbers: ")

numbers = [int(value.strip()) for value in comma_sep.split(",")]
numbers_tuple = tuple(numbers)

print(numbers)
print(numbers_tuple)




