#Temperature Convertet

#Define converison function
def celsius_to_fahrenheit(celsius):
    return ((celsius * 9/5) + 32)

def celsius_to_kelvin(celsius):
    return celsius+273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit -32) *5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit -32) *5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) *9/5 + 32

#display the menu
def show_menu():
    print("\n--- Temperature Converter Menu ---")
    print("1. Celsius to Fahrenheit & Kelvin")
    print("2. Fahrenheit to Celsius & Kelvin")
    print("3. Kelvin to Celsius & Fahrenheit")
    print("4. Exit")

while True:
    show_menu()
    choice = int(input("Enter your choice(1/2/3/4): "))

    if choice == 1:
        celsius = float(input("Enter temperature in Celsius: "))
        print(f"Fahrenheit: {celsius_to_fahrenheit(celsius):.2f}")
        print(f"Kelvin: {celsius_to_kelvin(celsius):.2f}")

    elif choice==2:
        fahrenheit=float(input("Enter temperature in Fahrenheit: "))
        print(f"Celsius: {fahrenheit_to_celsius(fahrenheit):.2f}")
        print(f"Kelvin: {fahrenheit_to_kelvin(fahrenheit):.2f}")
    elif choice == 3:
        kelvin = float(input("Enter temperature in Kelvin: "))
        print(f"Celsius: {kelvin_to_celsius(kelvin):.2f}")
        print(f"Fahrenheit: {kelvin_to_fahrenheit(kelvin):.2f}")

    elif choice==4:
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
