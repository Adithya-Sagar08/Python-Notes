import sys

pin = "1234"
balance = 50000
attempts = 0
max_attempts = 3
transactions = []

# PIN Verification
while True:
    entered_pin = input("Enter your PIN: ")

    if entered_pin == pin:
        print("\nPIN verification successful!\n")
        break

    attempts += 1
    remaining = max_attempts - attempts

    print(f"Invalid PIN! Remaining attempts: {remaining}")

    if attempts >= max_attempts:
        print("Card is blocked due to maximum attempts exceeded.")
        sys.exit()


# Main Menu
while True:
    print("---------- ATM MENU ----------")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Last 4 Transactions")
    print("5. Exit")
    print("------------------------------")

    try:
        choice = int(input("Enter your choice: "))

    except ValueError:
        print("Invalid input! Please enter a number.\n")
        continue

    # Check Balance
    if choice == 1:
        print(f"\nYour current balance is: ₹{balance}\n")

    # Deposit
    elif choice == 2:
        try:
            amount = int(input("Enter amount to deposit: ₹"))

            if amount > 0:
                balance += amount

                transactions.append(
                    f"Deposited: ₹{amount}"
                )

                if len(transactions) > 4:
                    transactions.pop(0)

                print(f"₹{amount} deposited successfully.")
                print(f"Current balance: ₹{balance}\n")

            else:
                print("Amount must be greater than 0.\n")

        except ValueError:
            print("Invalid amount! Please enter a number.\n")

    # Withdraw
    elif choice == 3:
        try:
            amount = int(input("Enter amount to withdraw: ₹"))

            if amount <= 0:
                print("Amount must be greater than 0.\n")

            elif amount > balance:
                print("Insufficient balance.\n")

            else:
                balance -= amount

                transactions.append(
                    f"Withdrawn: ₹{amount}"
                )

                if len(transactions) > 4:
                    transactions.pop(0)

                print(f"₹{amount} withdrawn successfully.")
                print(f"Current balance: ₹{balance}\n")

        except ValueError:
            print("Invalid amount! Please enter a number.\n")

    # Transaction History
    elif choice == 4:
        print("\n----- Last 4 Transactions -----")

        if transactions:
            for transaction in transactions:
                print(transaction)
        else:
            print("No transactions available.")

        print("--------------------------------\n")

    # Exit
    elif choice == 5:
        print("\nThank you for using the ATM!")
        break

    # Invalid Choice
    else:
        print("Invalid choice! Please select 1 to 5.\n")


print("End of the ATM Project.")