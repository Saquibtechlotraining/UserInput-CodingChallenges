# Body mass index (BMI) is a measure of body fat based on height and weight that applies to adult men and women.
# The Table below shows how healthy you are with respect to your BMI.

def calculate_BMI(weigth, height):

    BMI = round(weigth/height**2 * 1000)

    if BMI <= 18.5:
        return ("Underweight")

    if BMI > 18.5 and BMI <= 24.9:
        return ("Normal Weight")

    if BMI > 25.0 and BMI <= 29.9:
        return ("Overweight")

    else:
        return ("Obese")

if __name__=="__main__":
    weigth = float(input("Enter the weight:"))
    height = float(input("Enter the height:"))
    print("Calculate the BMI:", calculate_BMI(weigth, height))