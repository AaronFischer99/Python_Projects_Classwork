def view_balance(balance):
    print(f"Your current balance is ${balance:.2f}.")

def withdrawal(balance, amount):
    if amount > balance:
        print(f"Insufficient funds. Your balance is: ${balance:.2f}.")
    else:
        balance -= amount
        print(f"${amount:.2f} has been debited from your account.")
        print(f"\nYour new balance is: ${balance:.2f}.")

    return balance

def deposit(balance, amount):
    balance += amount
    print(f"${amount:.2f} has been credited to your account.")
    print(f"\nYour new balance is: ${balance:.2f}.")

    return balance

def main():
    balance = 100.00

    while True:
        print("\nWhat would you like to do?\n")
        print("1) View current balance")
        print("2) Record a debit (withdraw)")
        print("3) Record a credit (deposit)")
        print("4) Exit")

        choice = input("\nYour choice? ")

        if choice == '1':
            view_balance(balance)
        elif choice == '2':
            amount = float(input("\nHow much do you wish to withdraw? $"))
            balance = withdrawal(balance, amount)
        elif choice == '3':
            amount = float(input("\nHow much do you wish to deposit? $"))
            balance = deposit(balance, amount)
        elif choice == '4':
            print("\nThank you for using our ATM services!")
            break
        else:
            print(f"Invalid choice: {choice}")

    # Save the results to a text file
    with open("atm_results.txt", "w") as atm_file:
        atm_file.write(f"Final Balance: ${balance:.2f}")

if __name__ == "__main__":
    main()
