
from datetime import datetime
class Income:
    
    
    def __init__(self, income_id, amount, category, date=None):
        
        self.income_id = income_id
        self.amount = amount
        self.category = category
        self.date = date if date else datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        
        
    def get_income_amount(self):
        
        return self.amount
        
    def __str__(self):
            
        return f'Income ID: {self.income_id}\nAmount: {self.amount}\nCategory: {self.category}\nDate: {self.date}'
    
    def __repr__(self):
        
        return f'Income ID: {self.income_id}\nAmount: {self.amount}\nCategory: {self.category}\nDate: {self.date}'
    
    
    def __eq__(self, other):
        
        return self.income_id == other.income_id
    
    def __lt__(self, other):
            
        return self.amount < other.amount
    
    def __gt__(self, other):
        
        return self.amount > other.amount
    
    
    def __le__(self, other):
            
        return self.amount <= other.amount
    
    def __ge__(self, other):
        
        return self.amount >= other.amount

        
class ManageIncome:
    
    
    def __init__(self):
        
        self.income_dict = {}
        self.total_income = self.get_total_income()
        
        
    def add_income(self, income):
        
        self.income_dict[income.income_id] = income
        
        
    def get_income(self):
            
        return self.income_dict
    
    
    def get_total_income(self):
        
        total = 0
        for value in self.income_dict.values():
            total += value.amount
            
        return total
    
    
    
if __name__ == "__main__":
    
    income1 = Income(1, 1000, "Salary")
    income2 = Income(2, 500, "Bonus")
    income3 = Income(3, 200, "Interest")
    
    manage_income = ManageIncome()
    manage_income.add_income(income1)
    manage_income.add_income(income2)
    manage_income.add_income(income3)
    
    print(manage_income.get_income())
    print(manage_income.get_total_income())