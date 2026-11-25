"""Write a Python program to count the frequency of each word in a sentence."""


sentence = ["MY", "NAME", "IS","BLESSED", "AGE", "IS", "22", "GRADE", "IS", "22"]
count =0
word_to_search = input()

for word in sentence:
    if word == word_to_search: 
        count +=1
print(f"{count}")

