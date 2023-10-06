# Write a Python program that asks the user to enter a weight in kilograms,
# and then converts the weight to pounds and prints out the result.
# (Hint: the formula for converting kilograms to pounds is lb = kg * 2.2046):-

def kg_to_pounds(kg):
    pounds = kg * 2.2046
    return pounds

if __name__=="__main__":
    kg = float(input("Enter the weight in kg:"))
    print("Weight in Pounds:", kg_to_pounds(kg), "lb")