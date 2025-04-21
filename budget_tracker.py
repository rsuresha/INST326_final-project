class Transaction:
    """
    This class represents a singular transaction.
    """
    def __init__(self, date, category, amount, description):
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

    def get_total_spending(self):
        total = 0
    
        for amount in self.transactions:
            total += amount

        return amount