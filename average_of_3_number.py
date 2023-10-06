# Write a Python program that asks the user to enter three numbers,
# and then calculates and prints out the average of the three numbers.

def average(first_no, second_no, third_no):

    average = (first_no + second_no + third_no)/3
    return average

if __name__=="__main__":
    first_no = int(input("Enter the first number:"))
    second_no = int(input("Enter the second number:"))
    third_no = int(input("Enter the third number:"))
    print("The average of 3 numbers:", average(first_no, second_no, third_no))