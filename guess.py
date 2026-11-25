word = "apple"

guess = input("Guess a letter: ")

if guess not in word:
    print("YES")
else:
    print("NO")