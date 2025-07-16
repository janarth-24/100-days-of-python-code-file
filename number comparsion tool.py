# Number Comparison Tool
#Get user input for two numbers
no_of_num=int(input("How many number to compare (2 or 3) "))

if no_of_num==2:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

     #Compare the numbers
    print("\n--- Comparison Results ----")

    if num1 == num2:
      print(f"Both numbers are equal: {num1}")
    elif num1 > num2:
        print(f"{num1} is greater than {num2}")
    else:
        print(f"{num2} is greater than {num1}")
elif no_of_num==3:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))
    print("\n--- Comparison Results ----")
    if num1 > num2 and num1>num3:
        print(f"{num1} is greater than {num2} and {num3}")
    elif num2>num3 and num2>num1:
        print(f"{num2} is greater than {num1} and {num3}")
    elif num3>num1 and num3>num2:
        print(f"{num3} is greater than {num1} and {num2}")
    else:
        print("All the three number is equal")
else:
    print("Enter vaild input")
# Step 3: Check if any number is zero
if num1 == 0 or num2 == 0 or num3==0:
    print("\nAt least one number is zero.")
else:
    print("\nAll numbers are non-zero.")