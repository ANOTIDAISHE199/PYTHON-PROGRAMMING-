#Write a Python program that generates a random number between 1 and 9 and asks the user to guess it.
 #Display whether the guess is too high, too low, or correct#

import random

number = random.randint(1, 9)
print(number)
guess = 0
print("Guess the number")


guess = int(input())

if guess == number:
    print("correct")
elif guess > number:
    print("too high")
else:
    print("too low")


