


class Budget:
    
    
    def __init__(self,initial_balance):
        
        self.initial_balance = initial_balance
        self.current_balance = initial_balance
        
    def add_balance(self,amount):
        
        self.current_balance += amount
        
    def withdraw_balance(self,amount):
        
        self.current_balance -= amount
        
    def check_balance(self):
            
        return self.current_balance
    
