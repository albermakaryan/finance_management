
from datetime import datetime
class Expense:
    
    
    def __init__(self, expense_id, amount, category, date=None):
        
        self.expense_id = expense_id
        self.amount = amount
        self.category = category
        self.date = date if date else datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        
        
    def get_expense_amount(self):
        
        return self.amount
        
    def __str__(self):
            
        return f'Expense ID: {self.expense_id}\nAmount: {self.amount}\nCategory: {self.category}\nDate: {self.date}'
    
    def __repr__(self):
        
        return f'Expense ID: {self.expense_id}\nAmount: {self.amount}\nCategory: {self.category}\nDate: {self.date}'
    
    
    def __eq__(self, other):
        
        return self.expense_id == other.expense_id
    
    def __lt__(self, other):
            
        return self.amount < other.amount
    
    def __gt__(self, other):
        
        return self.amount > other.amount
    
    
    def __le__(self, other):
            
        return self.amount <= other.amount
    
    def __ge__(self, other):
        
        return self.amount >= other.amount

        
class ManageExpense:
    
    
    def __init__(self):
        
        self.expense_dict = {}
        self.total_expense = self.get_total_expense()
        
        
    def add_expense(self, expense):
        
        self.expense_dict[expense.expense_id] = expense
        
        
    def get_expense(self):
            
        return self.expense_dict
    
    
    def get_total_expense(self):
        
        total = 0
        for value in self.expense_dict.values():
            total += value.amount
            
        return total
    
    
    
if __name__ == "__main__":
    
    
    expense1 = Expense(1, 100, 'Food')
    expense2 = Expense(2, 200, 'Transport')
    expense3 = Expense(3, 300, 'Entertainment')
    
    manage_expense = ManageExpense()
    manage_expense.add_expense(expense1)
    manage_expense.add_expense(expense2)
    manage_expense.add_expense(expense3)
    
    print(manage_expense.get_expense())
    print(manage_expense.get_total_expense())