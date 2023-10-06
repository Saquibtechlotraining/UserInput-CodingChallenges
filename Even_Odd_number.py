# Write a Python program that asks the user to enter a number,
# and then prints out whether the number is even or odd:-

def even_odd(number):
    if number % 2 == 0:
        return "Even number"

    else:
        return "Odd number"

if __name__=="__main__":
    number = int(input("Enter the number:"))
    print(even_odd(number))