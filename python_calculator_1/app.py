import sys

def add(): 
    try: 
        num1 = input("Enter First Number: ")
        num2 = input("Enter Second Number: ")
        ans = float(num1) + float(num2) 
    except ValueError: 
        print("Please Enter Numbers Only")
        print()
        start()
    except Exception: 
        print("Something Went Wrong...")
        print()
        start()
    else: 
        print("=> " + str(ans))
        print()
        start()

def multiply(): 
    try: 
        num1 = input("Enter First Number: ")
        num2 = input("Enter Second Number: ")
        ans = float(num1) * float(num2)
    except ValueError: 
        print("Please Enter Numbers Only")
        print()
        start()
    except Exception: 
        print("Something Went Wrong...")
        print()
        start()
    else: 
        print("=> " + str(ans))
        print()
        start()

def subtract(): 
    try: 
        num1 = input("Enter First Number: ")
        num2 = input("Enter Second Number: ")
        ans = float(num1) - float(num2)
    except ValueError: 
        print("Please Enter Numbers Only")
        print()
        start()
    except Exception: 
        print("Something Went Wrong...")
        print()
        start()
    else: 
        print("=> " + str(ans)) 
        print()
        start()

def divide(): 
    try: 
        num1 = input("Enter Numerator: ")
        num2 = input("Enter Denominator: ")
        ans = float(num1) / float(num2)
    except ValueError: 
        print("Please Enter Numbers Only")
        print()
        start()
    except ZeroDivisionError: 
        print("Can't Divide by Zero")
        print()
        start()
    except Exception: 
        print("Something Went Wrong...")
        print()
        start()
    else: 
        print("=> " + str(ans))
        print()
        start()

def start():
    try: 
        action = input("Enter Action: (+, -, *, /, exit) ")
    
        if action == "+" or action == "add": 
            add()
        elif action == "-" or action == "subtract": 
            subtract()
        elif action == "*" or action == "multiply": 
            multiply()
        elif action == "/" or action == "divide": 
            divide()
        elif action == "exit" or action == "bye": 
            print("Bye...")
            sys.exit()
        elif action == "restart": 
            intro()
            start()
        else: 
            print("Please enter a valid action...")
            print()
            start()
    except KeyboardInterrupt: 
        print()
        print("Bye...")
        sys.exit()

def intro(): 
    print()
    print(" _________        .__               .__          __                 ")
    print(" \_   ___ \_____  |  |   ____  __ __|  | _____ _/  |_  ___________  ")
    print(" /    \  \/\__  \ |  | _/ ___\|  |  \  | \__  \    __\/  _ \_  __ \ ") 
    print(" \     \____/ __ \|  |_\  \___|  |  /  |__/ __ \|  | (  <_> )  | \/ ")
    print("  \______  (____  /____/\___  >____/|____(____  /__|  \____/|__|    ")
    print("         \/     \/          \/                \/                    ")
    print()
    print("Welcome to Calculator, ")
    print()

intro()
start()
