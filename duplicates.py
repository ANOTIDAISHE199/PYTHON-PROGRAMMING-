"""Given two lists, write a Python program to find the common elements between them without duplicates.
"""

list1 = [1 , 5,8,9,4]
list2 = [3,4,5,6,7,8]

for i in list2:
    if i in list1:
        print(i)