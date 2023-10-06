# Write a Python program that asks the user to enter two numbers, and then prints out the sum of the two numbers:-

def sum_of(first_number, second_number):

    sum = first_number + second_number
    return sum

if __name__=="__main__":
    first_number = int(input("Enter the first number:"))
    second_number = int(input("Enter the second number:"))
    print("The sum of two numbers:", sum_of(first_number, second_number))