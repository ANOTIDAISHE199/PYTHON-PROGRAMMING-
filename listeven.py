"""Write a Python program to create a new list containing only the even elements from a given list"""

list1 = [1,5,6,7,8,9,4,9]
new_list= []

for i in list1:
    if i % 2 == 0 :
        new_list = i
        print(new_list)