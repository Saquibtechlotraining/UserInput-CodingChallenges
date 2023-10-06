# Take Principle, Rate, and Interest From User and Calculate Simple Interest.
# Formulae For Simple Interest is:-

def calculate_simple_interest(principle, rate, time):

    Simple_Interset = (principle * rate * time)/100

    return Simple_Interset

if __name__=="__main__":
    principle = int(input('Enter the principle:'))
    rate = int(input("Enter the rate:"))
    time = int(input("Enter the time:"))
    print("Simple Interest:", calculate_simple_interest(principle, rate, time))