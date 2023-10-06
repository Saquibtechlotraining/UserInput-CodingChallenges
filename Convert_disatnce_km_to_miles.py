# Write a Python program that asks the user to enter a distance in kilometers,
# and then converts the distance to miles and prints out the result.
# (Hint: the formula for converting kilometers to miles is mi = km / 1.609):-

def km_to_miles(kilometer):
    miles = kilometer / 1.609
    return miles

if __name__=="__main__":
    kilometer = float(input("Enter the distance in kilometer:"))
print("Distance in Miles:", km_to_miles(kilometer), "miles")