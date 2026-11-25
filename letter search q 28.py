word = input("enter a word")
letter_to_search = input()

count = 0 

for i in word:
    if i  == letter_to_search:
        count += 1
        i =+ 1
print(count)
