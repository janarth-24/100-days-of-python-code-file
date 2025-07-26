#Safe calculator

#Show the menu for calulator
def show_menu():
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentiation")
    print("6. Percentage")
    print("7. Exit")

def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def mul(num1,num2):
    return num1*num2

def div(num1,num2):
    return num1/num2

def exp(num1,num2):
    return num1**num2

def per(num1,num2):
    return (num1/num2)*100

while True:
    show_menu()
    choice=int(input("Enter the choice (1-7):"))
    if choice==7:
        print("Exiting the Calculator! GoodBye.")
    try:
        if choice==1:
            num1 = int(input("Eneter the value for number 1: "))
            num2 = int(input("Eneter the value for number 2: "))
            print(f"Result :{ add(num1,num2)}")
        elif choice==2:
            num1 = int(input("Eneter the value for number 1: "))
            num2 = int(input("Eneter the value for number 2: "))
            print(f"Result :{ sub(num1,num2)}")
        elif choice==3:
            num1 = int(input("Eneter the value for number 1: "))
            num2 = int(input("Eneter the value for number 2: "))
            print(f"Result :{ mul(num1,num2)}")
        elif choice==4:
            num1 = int(input("Eneter the value for number 1: "))
            num2 = int(input("Eneter the value for number 2: "))
            print(f"Result :{ div(num1,num2)}")
        elif choice==5:
            num1 = int(input("Eneter the value for base: "))
            num2 = int(input("Eneter the value for power: "))
            print(f"Result :{ exp(num1,num2)}")
        elif choice==6:
            num1 = int(input("Eneter the value for value: "))
            num2 = int(input("Eneter the value for total: "))
            print(f"Result :{ per(num1,num2)}")
        else:
            print("Invaild input! enter the choice(1-7) ")
    except ZeroDivisionError as e:
        print(f"Error:{e}")
    except Exception as e:
        print(f"An unecepted error occured: {e}")
    finally:
        print("Thank you using Calculator..... Restarting")