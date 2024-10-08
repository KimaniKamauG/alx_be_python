FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5    

def convert_to_celsius(fahrenheit):
    """"Convert Fahrenheit to Celsius"""
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """"Convert Celsius to Fahrenheit"""
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

temperature = float(input('Enter the temperature to convert:'))
temp_type = input('Is this temperature in Celsius or Fahrenheit? (C/F): ').strip().upper()

if temp_type == 'C':
    converted_temp = convert_to_fahrenheit(temperature)
    print(f'{temperature}°C is {converted_temp}°F')
elif temp_type == 'F':
    converted_temp = convert_to_celsius(temperature)
    print(f'{temperature}°F is {converted_temp}°C')
else:
    print('Invalid temperature. Please enter a numeric value.')



