# Write a Python program that asks the user to enter a number,
# and then checks whether the number is a perfect square or not.
# (Hint: a perfect square is a number that is equal to the square of an integer)
#To solve this problem we use sqrt module:-

number = int(input("Enter the number:"))
from math import sqrt

s = int(sqrt(number))
value = s * s

if value == number:
    print("Perfect Square Number")
else:
    print("Not a perfect Square number")
