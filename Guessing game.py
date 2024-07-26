def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def convert_celsius(celsius):
    fahrenheit = celsius_to_fahrenheit(celsius)
    kelvin = celsius_to_kelvin(celsius)
    return fahrenheit, kelvin

def main():
    try:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit, kelvin = convert_celsius(celsius)
        print(f"{celsius}°C is equal to {fahrenheit}°F and {kelvin}K.")
    except ValueError:
        print("Please enter a valid number.")

if name == "main":
    main()
