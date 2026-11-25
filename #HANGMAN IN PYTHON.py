#HANGMAN IN PYTHON
import random

WORDS = ("apple", "orange", "banana", "coconut", "pineapple")
MAX_WRONG = 6

HANGMAN_ART = {
    0: ("   ",
        "   ",
        "   "),
    1: (" O ",
        "   ",
        "   "),
    2: (" O ",
        " | ",
        "   "),
    3: (" O ",
        "/| ",
        "   "),
    4: (" O ",
        "/|\\",
        "   "),
    5: (" O ",
        "/|\\",
        "/  "),
    6: (" O ",
        "/|\\",
        "/ \\"),
}


def display_man(wrong_guesses):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for line in HANGMAN_ART[wrong_guesses]:
        print(line)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


def display_hint(hint):
    print(" ".join(hint))


def main():
    answer = random.choice(WORDS)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()

    while True:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input")
            continue

        if guess in guessed_letters:
            print(f"{guess} already guessed")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i, letter in enumerate(answer):
                if letter == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_hint(hint)
            print("YOU WIN!")
            break

        if wrong_guesses >= MAX_WRONG:
            display_man(wrong_guesses)
            print(f"YOU LOSE! The word was: {answer}")
            break


if __name__ == "__main__":
    main()