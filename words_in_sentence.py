# Write a Python program that asks the user to enter a string, and then prints out the length of the string:-

sentence = input("Enter the sentence:")
result = []
for i in sentence:
    if i.isalpha():
        result.append(i)
print(len(result))