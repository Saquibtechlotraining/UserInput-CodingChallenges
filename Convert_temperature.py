# Take Temperature in fahreinheit and convert it into celcius:-

def convert_temperature(fahreinheit):
    Celsius = (fahreinheit -32)*5 /9
    return int(Celsius)

if __name__ == "__main__":
    fahreinheit = float(input("Enter the temperature in fahreinheit:"))
    print("Temperature in Celcius:", convert_temperature(fahreinheit))