
file = open("temperature.txt", "r")
data = file.readline()  
temperatures = data.split(",")
i = 0
total = 0
print("The temperatures are:")
while i < len(temperatures):
    temperature = float(temperatures[i])  
    if temperature > 29:
        print("   {} ** higher than 29!!!".format(temperature))
    else:
        print("   {}".format(temperature))
    total += temperature
    i += 1
average = total / len(temperatures)
print("Number of readings:", len(temperatures))
print("Average temperature: {:.2f}".format(average))
file.close
