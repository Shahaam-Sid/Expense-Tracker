import colorama as cr
from Expense import Expense
from LoadData import LoadData

cr.init(autoreset=True)

try:
    print(cr.Fore.BLUE + cr.Style.BRIGHT + "----- EXPENSE TRACKING APP -----")
    while True:
        print(cr.Fore.BLUE + """
Input Any of The Following:
1 -- New Expense
2 -- Check Expense
3 -- Quit App
""")
        
        choice = input(cr.Fore.GREEN + "Enter you choice(1, 2 or 3)> ")
         
        match choice:
            case "1": 
                title = input(cr.Fore.GREEN + "Enter Title(20 Characters Max): ")
                cost = float(cr.Fore.GREEN + input("Enter Cost: "))
                note = input(cr.Fore.GREEN + "Write Short Explainatory Note(50 Characters Max): ")
                
                currenttd = input(cr.Fore.BLUE + "Do You Want Current Time & Date(Y or N): ").upper()
                
                if currenttd == "Y":
                    x = Expense(title, cost, note)
                
                else:
                    print("""
Time must be in 24-Hour Format
Enter Time Like 'hour:minute' i.e '09:42'
Enter Date Like  'DD-Mon-YYYY' i.e '06-jul-2005'                 
                          """)
                    
                    time = input(cr.Fore.GREEN + "Enter Time: ")
                    date = input(cr.Fore.GREEN + "Enter Date: ")
                    
                    x = Expense(title, cost, note, date, time)

                y = LoadData(x)
                y.store_to_json()
                print(cr.Fore.GREEN + cr.Style.BRIGHT + "Expense Added")
                print()
            
            case "2":
                month = int(input(cr.Fore.GREEN + "Enter Month(1-12): "))
                year = int(input(cr.Fore.GREEN + "Enter Year: "))
                
                z = LoadData.extract_from_json(month, year)
                LoadData.display_data(z)
                
            case "3":
                break
            case _:
                print(cr.Back.RED + cr.Fore.WHITE + "Invalid Input")
    
except TypeError as e:
    print(f"{cr.Back.RED}{cr.Fore.WHITE}Error: {e}")
    
except ValueError as e:
    print(f"{cr.Back.RED}{cr.Fore.WHITE}Error: {e}")
    
except Exception as e:
    print(cr.Back.RED + cr.Fore.WHITE + "Unexpected Error")

finally:
    print(cr.Fore.BLUE + cr.Style.BRIGHT + "----- Program -- End -----")