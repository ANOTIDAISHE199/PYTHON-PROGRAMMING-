"""Write a Python program to check whether a given letter is a vowel or not.
"""

speach = str(input().lower)
list1 = list(speach)
list2 = ["a", "e",  "i" ,"o", "u"]

if list1 in list2 :
    print(f"{speach} is a vowel")
else:
    print("not a vowel")