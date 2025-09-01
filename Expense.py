from datetime import datetime as d

class Expense:
    def __init__(self, title, cost, note):
        if not isinstance(title, str):
            raise TypeError("Title must be String")
        
        if not isinstance(cost, (int, float)):
            raise TypeError("Cost must be an Integer or Float value")
        
        if not isinstance(note, str):
            raise TypeError("Note must be a String")
        
        if len(title) == 0 or title.isspace() or title.isdigit():
            raise ValueError("Title must contains Words")
        
        if cost <= 0:
            raise ValueError("Cost cannot be 0 or less")
        
        if len(note) == 0 or note.isspace() or note.isdigit():
            raise ValueError("Title must contains Words")
        
        self.title = title
        self.cost = cost
        self.note = note
        
        dd = d.today().strftime("%d-%b-%Y")
        
        self.date = dd
        
        tt = d.now().strftime("%H:%M")
        
        self.time = tt
        
    def __str__(self):
        return f"{self.title}: Rs.{self.cost}, Time/Date: {self.time}/{self.date} note: {self.note}"
        
x = Expense("Test", 29, "Testing the class")
print(x)