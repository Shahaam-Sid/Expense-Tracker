import json
from Expense import Expense
from datetime import datetime as d

class LoadData:
    
    filepath = "tracker.json"
    
    def __init__(self, expense):
        self.expense = expense
        self._expenses = {}
        
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
            self._expenses = {}
            
        expense_date = d.strptime(self.expense.date, "%d-%b-%Y")
        year = str(expense_date.year)
        month = expense_date.strftime("%b")
        
        if year not in self._expenses:
            self._expenses[year] = {}
        if month not in self._expenses[year]:
            self._expenses[year][month] = []
        
        volatile_dict =  {
            "title": self.expense.title,
            "cost": self.expense.cost,
            "time": self.expense.time,
            "date": self.expense.date,
            "note": self.expense.note
        }
            
        self._expenses[year][month].append(volatile_dict)
            
        with open(self.filepath, 'w') as file:
            json.dump(self._expenses, file, indent=4)