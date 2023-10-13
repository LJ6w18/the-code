days = int(input("Please enter the number of days: "))
a = days + 1 
for i in range(1,a):
    if i % 7 == 1:
        print("{:3}|{}".format("Day","Task(s)"))
    print("{:3}|{}".format(i,''))