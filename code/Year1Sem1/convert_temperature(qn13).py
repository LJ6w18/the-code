def fahr_to_cel(fahrenheit):
    celsius = (5.0 / 9.0) * (fahrenheit - 32)
    return celsius

def cel_to_fahr(celsius):
    fahrenheit = (9.0 / 5.0) * celsius + 32
    return fahrenheit

while True:
    print("Temperature Conversion")
    print("[1] Fahrenheit to Celsius")
    print("[2] Celsius to Fahrenheit")
    print("[3] Exit")

    option = input("Please enter your option: ")

    if option == '1':
        fahrenheit = float(input("Please enter the temperature in Fahrenheit: "))
        celsius = fahr_to_cel(fahrenheit)
        print(f"The temperature in Celsius is {celsius:.1f} degrees.")
    elif option == '2':
        celsius = float(input("Please enter the temperature in Celsius: "))
        fahrenheit = cel_to_fahr(celsius)
        print(f"The temperature in Fahrenheit is {fahrenheit:.1f} degrees.")
    elif option == '3':
        break
    else:
        print("Invalid option. Please try again.")
