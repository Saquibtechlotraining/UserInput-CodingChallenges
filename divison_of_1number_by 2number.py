# Write a Python program that asks the user to enter two numbers,
# and then prints out the remainder of the division of the first number by the second number:-

def division(first_number, second_number):

    remainder = first_number % second_number
    return remainder

if __name__=="__main__":
    first_number = int(input("Enter the first number:"))
    second_number = int(input("Enter the second number:"))
    print("Remainder of the division of first number by the second_number:", division(first_number, second_number))
