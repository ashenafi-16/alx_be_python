FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(f):
    return FAHRENHEIT_TO_CELSIUS_FACTOR * (f - 32)

def convert_to_fahrenheit(c):
    return CELSIUS_TO_FAHRENHEIT_FACTOR * c + 32

temperature = int(input("Enter the temperature to convert: "))
choice = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

if choice == 'F':
    print(convert_to_celsius(temperature))
elif choice == 'C':
    print(convert_to_fahrenheit(temperature))
else:
    print("Invalid temperature. Please enter a numeric value.")
