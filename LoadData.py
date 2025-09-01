import json
from Expense import Expense
from datetime import datetime as d
import calendar

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
            
            
    @classmethod
    def extract_from_json(cls, month = 0, year = 0):
        if not isinstance(month, int):
            raise TypeError("Month can only be a Integer Value")
        
        if not isinstance(year, int):
            raise TypeError("Year can only be an Ineteger Value")
        
        if year < 0:
            raise ValueError("Year Cannot be a negative Value")
        
        if month < 0 or month > 12:
            raise ValueError("Month Cannit be less then zero and more the 12")
        
        try:
            with open(cls.filepath, 'r') as file:
                    expenses = json.load(file)
                    
        except (FileNotFoundError, json.JSONDecodeError):
            print("No Data Found")
            return {}
        
        if year == 0:
            return expenses
    
        year_str = str(year)
        if year_str not in expenses:
            print(f"No data for year {year}")
            return {}
    
        if month == 0:
            return expenses[year_str]
    
        month_str = calendar.month_abbr[month]
        if month_str not in expenses[year_str]:
            print(f"No data for {month_str} {year}")
            return {}
    
        return expenses[year_str][month_str]
            
        