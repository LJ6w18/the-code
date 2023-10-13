import random

count = 0
days = []

print("This program demonstrates the birthday paradox.")

while True:
    a = random.randint(1, 365)
    print("{} was randomly generated.".format(a))

    if a in days:
        print("Duplicate day! This took {} tries.".format(len(days)))
        break

    days.append(a)
