#Simple Calculator
while True:
    # Get the user input of operation
    print("\n======Calculator======")
    print("Which operation can perform")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Divison")
    print("5.Exit")
    operator = int(input("Enter the 1 to 5 for your calculation: "))
    if operator == 5:
        print("Exit from calculator")
        break

    # user input for two numbers
    num1 = int(input("Enter the First Number: "))
    num2 = int(input("Enter the Second Number: "))

    # Preform the Arithmetic operation
    if operator ==1:
        add=num1+num2
        print(f"Addition of number {num1} and {num2}: {add}")
    elif operator ==2:
        sub=num1-num2
        print(f"Subtraction of number {num1} and {num2}: {sub}")
    elif operator == 3:
        mul = num1 * num2
        print(f"Multiplication of number {num1} and {num2}: {mul}")
    elif operator ==4:
        if num2==0:
            print("Zero is cannot be divide")
        else:
            div=num1/num2
            print(f"Divison of number {num1} and {num2}: {div}")
    else:
        print("Invaild Input! Enter the correct input")




