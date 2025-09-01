from datetime import datetime as d

class Expense:
    def __init__(self, title, cost, note):

        self.title = title
        self.cost = cost
        self.note = note
        
        dd = d.today().strftime("%d-%b-%Y")
        
        self._date = dd
        
        tt = d.now().strftime("%H:%M")
        
        self._time = tt
        
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
        
        if len(value) == 0 or value.isspace() or value.isdigit():
            raise ValueError("Title must contains Words")
        
        self._title = value
        
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
        
        self._note = value
        
    def __str__(self):
        return f"{self.title}: Rs.{self.cost}, Time/Date: {self.time}/{self.date} note: {self.note}"
