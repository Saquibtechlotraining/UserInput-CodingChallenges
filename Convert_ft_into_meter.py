# Write a Python program that asks the user to enter a length in feet,
# and then converts the length to meters and prints out the result.
# (Hint: the formula for converting feet to meters is m = ft / 3.2808):-

def convert(length_in_feet):

    metre = length_in_feet/3.2808
    return metre

if __name__=="__main__":
    length_in_feet = float(input("Enter the length in feet:"))
    print("length in meters:", convert(length_in_feet), "metre")