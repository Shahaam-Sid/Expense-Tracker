import json
from Expense import Expense

class LoadData:
    
    filepath = "tracker.json"
    
    def __init__(self, expense):
        self.expense = expense
        self._expenses = []
        
    @property
    def expense(self):
        return self._expense

    @expense.setter
    def expense(self, value):
        if not isinstance(value, Expense):
            raise TypeError("Can only Load Expense")
        
        self._expense = value

            
    def store_to_json(self):
        
        try:
            with open(self.filepath, 'r') as file:
                self._expenses = json.load(file)
                
            
        except (FileNotFoundError, json.JSONDecodeError):
            self._expenses = []
        
        volatile_dict =  {
            "title": self.expense.title,
            "cost": self.expense.cost,
            "time": self.expense.time,
            "date": self.expense.date,
            "note": self.expense.note
        }
            
        self._expenses.append(volatile_dict)
            
        with open(self.filepath, 'w') as file:
            json.dump(self._expenses, file, indent=4)