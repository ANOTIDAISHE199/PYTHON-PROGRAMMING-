import random

SYMBOLS = ['C', 'W', 'O', 'B', 'S']
PAYOUTS = {'C': 3, 'W': 4, 'O': 5, 'B': 8, 'S': 10}


def spin_row():
    return [random.choice(SYMBOLS) for _ in range(3)]


def print_row(row):
    print("~~~~~~~~~~~~~")
    print(" * ".join(row))
    print("~~~~~~~~~~~~~")


def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        return bet * PAYOUTS[row[0]]
    return 0


def get_bet(balance):
    while True:
        raw = input(f"Place your bet (1-{balance}): ").strip()
        try:
            bet = int(raw)
        except ValueError:
            print("Please enter a valid whole number")
            continue
        if bet <= 0:
            print("Bet must be greater than 0")
        elif bet > balance:
            print("Insufficient balance")
        else:
            return bet


def main():
    balance = 100
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(" WELCOME TO PYTHON SLOTS ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(" Symbols:  C  W  O  B  S ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    while balance > 0:
        print(f"Current Balance: ${balance}")
        bet = get_bet(balance)
        balance -= bet

        print("SPINNING...\n")
        row = spin_row()
        print_row(row)

        payout = get_payout(row, bet)
        balance += payout

        if payout > 0:
            print(f"YOU WON ${payout}")
        else:
            print("SORRY YOU LOST THIS ROUND")

        if balance <= 0:
            print("You're out of money!")
            break

        if input("DO YOU WANT TO PLAY AGAIN? (Y/N): ").strip().upper() != 'Y':
            break

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("GAME OVER!!!!!!")
    print(f"Final balance: ${balance}")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


if __name__ == "__main__":
    main()