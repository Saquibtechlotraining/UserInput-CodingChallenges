# Tom had y amount in his bank and jeff withdrawn x amount where x is always less than y.
# Print the remaining balance in Tom's account. Take x and y from user.

tom_amount = int(input("Enter the tom amount in the bank:"))
jeff_amount = int(input("Enter the amount jeff withdrawn:"))

if jeff_amount < tom_amount:
    Toms_account_balance = tom_amount - jeff_amount
    print("Remaining balance in Tom's account:", Toms_account_balance)

else:
    print("Invalid Input")