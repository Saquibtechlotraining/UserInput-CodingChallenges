# Your task is to take name and age  and  location from user and print the following message  :
# Hello Everyone , I am xyz and i am xyz years old and i live in xyz:-

if __name__=="__main__":
    name = input("Enter the name:")
    age = int(input("Enter the age:"))
    location = input("Enter the location:")
    print("Hello Everyone, I am ", name, "and i am", age, "years old and i live in", location)
