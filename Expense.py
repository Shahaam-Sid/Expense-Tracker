from datetime import datetime as d

class Expense:
    def __init__(self, title, cost, note, date = None, time = None):

        self.title = title
        self.cost = cost
        self.note = note
        self.time = time
        self.date = date
        
    @property
    def title(self):
        return self._title
    
    @property
    def cost(self):
        return self._cost
    
    @property
    def note(self):
        return self._note
    
    @property
    def date(self):
        return self._date
    
    @property
    def time(self):
        return self._time
    
    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise TypeError("Title must be String")
        
        if len(value) == 0 or value.isspace():
            raise ValueError("Title must contains Words")
        
        if len(value) > 20:
            raise ValueError("Title must not be more than 20 letters")
        
        self._title = value.strip()
        
    @cost.setter
    def cost(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Cost must be an Integer or Float value")
        
        if value <= 0:
            raise ValueError("Cost cannot be 0 or less")
        
        self._cost = value
        
    @note.setter
    def note(self, value):
        if not isinstance(value, str):
            raise TypeError("Note must be a String")
        
        if len(value) == 0 or value.isspace() or value.isdigit():
            raise ValueError("Note must contains Words")
        
        if len(value) > 50:
            raise ValueError("Note must not be more than 50 letters")
        
        self._note = value.strip()
        
    @time.setter
    def time(self, value = None):
        if value is None:
            self._time = d.now().strftime("%H:%M")
        else:
            try:
                valid_time = d.strptime(value, "%H:%M")
                self._time = valid_time.strftime("%H:%M")
            except ValueError:
                raise ValueError("Time must be in HH:MM format (24-hour)")
            
    @date.setter
    def date(self, value = None):
        if value is None:
            self._date = d.now().strftime("%d-%b-%Y")
        else:
            try:
                valid_date = d.strptime(value, "%d-%b-%Y")
                self._date = valid_date.strftime("%d-%b-%Y")
            except ValueError:
                raise ValueError("Date must be in DD-Mon-YYYY format (e.g., 01-Sep-2025)")
        
    def __str__(self):
        return f"{self.title}: Rs.{self.cost}, Time/Date: {self.time}/{self.date} note: {self.note}"

    def __repr__ (self):
        return f"""
Expense(
    'title': "{self.title}",
    'cost': "{self.cost}",
    'time': "{self.time}",
    'date': "{self.date}",
    'note': "{self.note}"
)"""
