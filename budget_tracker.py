import json

class Transaction:
    """
    This class represents a singular transaction.
    """
    id_assigner = 1

    def __init__(self, date, category, amount, description):

        #Class level variable to assign each transaction a unique id
        self.id = Transaction.id_assigner

        Transaction.id_assigner += 1

        self.date = date
        self.category = category
        self.amount = amount
        self.description = description


class BudgetTracker:

    """
    This class represents a BudgetTracker object. A budget tracker will have a list of transactions 
    and provides basic functionality, including: printing a report, viewing total spending, 
    spending by category, and descriptions/notes regarding a specific transaction.

    """
    def __init__(self):
        self.transactions = []

    def add_transaction(self, date, category, amount, description):
        transaction = Transaction(date, category, amount, description)
        self.transactions.append(transaction)

    def get_net_spending(self):
        total = 0
    
        for transaction in self.transactions:
            total += transaction.amount

        return total
    
    def get_total_income(self):
        total = 0

        for transaction in self.transactions:
            if transaction.amount > 0:
                total += transaction.amount

        return total
    
    def get_total_expenses(self):
        total = 0

        for transaction in self.transactions:
            if transaction.amount < 0:
                total += transaction.amount

        return total
    
    
    def get_spending_by_category(self):
        #Generates a dict with spending by category
        spending = {}

        for transaction in self.transactions:
            if transaction.amount < 0:
                if transaction.category in spending:
                    spending[transaction.category] += transaction.amount
                else:
                    spending[transaction.category] = transaction.amount

        return spending
    
    def get_transactions_by_month(self, month, year):
        #Iterates thru the transaction list, and if a transaction date matches the parameter time frame,
        #add it to the resulting list of transactions 
        results = []

        for transaction in self.transactions:

            transaction_day, transaction_month, transaction_year = transaction.date.split("-")
        
        #Converts date information from str to int
            if int(transaction_month) == month and int(transaction_year) == year:
                results.append(transaction)

        return results
    
    def save_to_json(self, filename):
        data = []

        for transaction in self.transactions:
            data.append({
                "id" : transaction.id,
                "date": transaction.date,
                "category": transaction.category,
                "amount": transaction.amount,
                "description": transaction.description
            })

        with open(filename, "w") as f:
            json.dump(data, f, indent=4)


    def load_from_json(self, filename):
        #Loads in budget data from a json file
        with open(filename, "r") as f:
            data = json.load(f)

        self.transactions = []
        max_id = 0

        for item in data:

            transaction = Transaction(item["date"], item["category"], item["amount"], item["description"])
            transaction.id = item["id"]
            self.transactions.append(transaction)

            if transaction.id > max_id:
                max_id = transaction.id

        Transaction.id_assigner = max_id + 1

    def print_all_transactions(self):
        if not self.transactions:
            print("No transactions recorded.")
            return

        for t in self.transactions:
            print(f"[ID {t.id}] {t.date} | {t.category} | ${t.amount} | {t.description}")



    


