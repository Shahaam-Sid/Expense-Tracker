import json
from Expense import Expense
from datetime import datetime as d
import calendar

class LoadData:
    """
    A Class that Stores, Extracts and Displays
    Data from JSON file
    """
    
    filepath = "tracker.json"
    
    def __init__(self, expense):
        """
        Inputs Expense
        Allows to Store expense in json file
        can extract and display expenses from json file

        Args:
            expense (Expense)
        """
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
        """
        Store Data to json file
        """
        
        try:
            with open(self.__class__.filepath, 'r') as file:
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
            
        with open(self.__class__.filepath, 'w') as file:
            json.dump(self._expenses, file, indent=4)
            
            
    @classmethod
    def extract_from_json(cls, month = 0, year = 0):
        """Extracts Data from json file

        Args:
            month (int, float): Month for which required Expenses
            year (int, float): Year for the required Expenses

        Returns:
            List or Dictionaries
        """
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
            return {}
        
        if year == 0:
            return expenses
    
        year_str = str(year)
        if year_str not in expenses:
            return {}
    
        if month == 0:
            return expenses[year_str]
    
        month_str = calendar.month_abbr[month]
        if month_str not in expenses[year_str]:
            return {}
    
        return expenses[year_str][month_str]
    
    @staticmethod
    def display_data(expense):
        """
        Displays Data

        Args:
            expense (return of extract_from_json())
        """
        
        if not expense:
            print("No Expenses to Show")
            
        if isinstance(expense, list):
            for e in expense:
                print(f"{e['date']} | {e['time']} | {e['title']} | ${e['cost']} | {e['note']}")
                
        elif isinstance(expense, dict):
            for month, items in expense.items():
                print (f"--- {month} ---")
                for e in items:
                    print(f"{e['date']} | {e['time']} | {e['title']} | ${e['cost']} | {e['note']}")
                    
        else:
            raise ValueError("Wrong Input")
            