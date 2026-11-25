def show_balance():
    print(f"YOUR BALANCE IS ${balance: .2f}")

def deposit():
    amount = float(input("ENTER AMOUNT TO BE DEPOSITED: "))

    if amount < 0 :
        print("INVALID INPUT")
        return 0
    else:
        return amount
def withdraw():
    amount = int(input("ENTER AMOUNT TO BE WITHDRAWN: "))

    if amount > balance:
        print("AMOUNT TO WITHDRAW CAN NOT EXCEED THE CURRENT BALANCE")
        return 0 
    elif amount < 0:
        print("amount must be greater than 0")
        return 0
    else:
        print(f"{amount} withdrawn from the account")
        print(f"NEW BALANCE: {balance - amount}")
        
balance = 0
is_running = True

while is_running:
    print("BANKING PROGRAM")
    print("1. SHOW BALANCE")
    print("2. DEPOSIT")
    print("3. WITHDRAW")
    print("4. EXIT")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        show_balance()
    elif choice == '2':
        balance += deposit()
    elif choice == '3':
        withdraw()
    elif choice == '4':
        is_running = False
    else:
        print("INVALID CHOICE")
