# Suppose there are many N numbers of people in the Army.
# We need to distribute them in G groups.
# Take the number of people from users and the Number of Groups and tell how many are left without Group:-
def calculate_people(number_of_people, group):
    people = number_of_people % group
    return people

if __name__=="__main__":
    number_of_people = int(input("Enter the number of people:"))
    group = int(input("Enter the group:"))
    print("Left people without group:", calculate_people(number_of_people, group))