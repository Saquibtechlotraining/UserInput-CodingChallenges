# Write a Python program that asks the user to enter a temperature in Celsius,
# and then converts the temperature to Fahrenheit and prints out the result.
# (Hint: the formula for converting Celsius to Fahrenheit is F = (C * 9/5) + 32):-

def convert_temp(celsius):
    fahrenheit = (celsius * 9/5)+32
    return fahrenheit

if __name__=="__main__":
    celsius = int(input("Enter the temperature in celsius:"))
    print("Temperature in fahrenheit:", convert_temp(celsius), "F")