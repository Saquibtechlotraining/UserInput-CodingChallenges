# Take input of the length and breadth of a rectangle from the user and print the area of it:-

def Area_of_rectangle(lenght, breadth):
    output = length * breadth
    return output

if __name__=="__main__":
    length = float(input("Enter the length of a rectangle:"))
    breadth = float(input("Enter the breadth of a rectangle:"))
    print("The area of a rectangle:", Area_of_rectangle(length, breadth))