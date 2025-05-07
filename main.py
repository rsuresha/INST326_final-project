from budget_tracker import BudgetTracker

def print_budget_menu():
    print("\n=== Budget Tracker Menu ===")
    print("1. Add a new transaction")
    print("2. View all transactions")
    print("3. View total income")
    print("4. View total expenses")
    print("5. View net balance")
    print("6. View spending by category")
    print("7. View transactions by month")
    print("8. Save transactions to file")
    print("9. Load transactions from file")
    print("0. Exit")

def run_cli():
    tracker = BudgetTracker()

    while True:
        print_budget_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            date = input("Enter the date (DD-MM-YYYY): ")
            category = input("Enter the category: ")
            amount = float(input("Enter the amount (negative for expenses): "))
            description = input("Enter the memo: ")
            tracker.add_transaction(date, category, amount, description)
            print("Transaction added successfully!")

        elif choice == '2':
            if not tracker.transactions:
                print("No transactions recorded.")
            else:
                print("\nAll Transactions:")
                for t in tracker.transactions:
                    print(f"[ID {t.id}] {t.date} | {t.category} | ${t.amount:.2f} | {t.description}")

        elif choice == '3':
            print(f"Total income: ${tracker.get_total_income():.2f}")

        elif choice == '4':
            print(f"Total expenses: ${tracker.get_total_expenses():.2f}")

        elif choice == '5':
            print(f"Net balance: ${tracker.get_net_spending():.2f}")

        elif choice == '6':
            spending = tracker.get_spending_by_category()
            #if no existing data exists
            if not spending:
                print("No expense data available.")
            else:
                print("\nSpending by Category:")
                for category, amount in spending.items():
                    print(f"{category}: ${amount:.2f}")

        elif choice == '7':
            month = int(input("Enter month (as number): "))
            year = int(input("Enter year: "))
            results = tracker.get_transactions_by_month(month, year)

            #if no transactions exist
            if not results:
                print("No transactions found for that month and year.")
            else:
                print(f"\nTransactions for {month}-{year}:")

                #iterate thru the results list and print each transaction
                for t in results:
                    print(f"[ID {t.id}] {t.date} | {t.category} | ${t.amount} | {t.description}")


        elif choice == '0':
            exit()

if __name__ == "__main__":
    run_cli()
