from Expense import Expense
from LoadData import LoadData

try:
    print("----- EXPENSE TRACKING APP -----")
    while True:
        print("""
Input Any of The Following:
1 -- New Expense
2 -- Check Expense
3 -- Quit App
""")
        
        choice = input("Enter you choice(1, 2 or 3)> ")
         
        match choice:
            case "1": 
                title = input("Enter Title(20 Characters Max): ")
                cost = float(input("Enter Cost: "))
                note = input("Write Short Explainatory Note(50 Characters Max): ")
                
                currenttd = input("Do You Want Current Time & Date(Y or N): ").upper()
                
                if currenttd == "Y":
                    x = Expense(title, cost, note)
                
                else:
                    print("""
Time must be in 24-Hour Format
Enter Time Like 'hour:minute' i.e '09:42'
Enter Date Like  'DD-Mon-YYYY' i.e '06-jul-2005'                 
                          """)
                    
                    time = input("Enter Time: ")
                    date = input("Enter Date: ")
                    
                    x = Expense(title, cost, note, date, time)

                y = LoadData(x)
                y.store_to_json()
                print("Expense Added")
                print()
            
            case "2":
                month = int(input("Enter Month(1-12): "))
                year = int(input("Enter Year: "))
                
                z = LoadData.extract_from_json(month, year)
                LoadData.display_data(z)
                
            case "3":
                break
            case _:
                print("Invalid Input")
    
except TypeError as e:
    print("Error: ", e)
    
except ValueError as e:
    print("Error: ", e)
    
except Exception as e:
    print("Unexpected Error")

finally:
    print("----- Program -- End -----")