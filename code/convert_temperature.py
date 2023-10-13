TempC = int(input("Enter the temprature in degree celcius:"))
def convert_temperature():
    TempF = (TempC * 9 / 5) + 32
    return TempF
print('The temperature is equivalent to {} fahrenheit.'.format(convert_temperature()))