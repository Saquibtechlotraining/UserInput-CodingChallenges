# Write a program to find the number of particular percentage number:-

number = int(input("Enter the number of which a percentage we want:"))
percentage_number = int(input("Enter the % number:"))

result = number * (percentage_number/100)
print("The", percentage_number, "% of", number, "is", result)
