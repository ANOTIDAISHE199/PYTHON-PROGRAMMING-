""" Write a Python program to check whether a given string is a palindrome or not using slicing."""

word = input()

list1 = list(word)



if list1 == list1[::-1]: 
    print("palindrom")
else:
    print("not a palindrom")