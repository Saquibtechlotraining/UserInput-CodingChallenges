# Write a Python program that asks the user to enter a temperature in Celsius,
# and then converts the temperature to Kelvin and prints out the result.
# (Hint: the formula for converting Celsius to Kelvin is K = C + 273.15):-

def  celsius_to_kelvin(temp_in_celsius):
    kelvin = temp_in_celsius + 273.15
    return kelvin

if __name__=="__main__":
    temp_in_celsius = float(input("Enter the celsius temperature:"))
    print("Temperature in Kelvin:", celsius_to_kelvin(temp_in_celsius), "K")