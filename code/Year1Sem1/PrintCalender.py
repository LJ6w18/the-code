a = int(input("Enter the number of days:"))
b = input("when is the first day of the week:")
week = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
index = week.index(b.capitalize())
print()
print('{:>4}{:>4}{:>4}{:>4}{:>4}{:>4}{:>4}'.format('Sun','Mon','Tue','Wed','Thu','Fri','Sat'))
d=1
while d <= int(a):
    for i in range(7):
        if d > int(a):
            break
        elif d == 1 and i < index:
            print("{:4}".format(''),end="")
            continue

        print("{:4}".format(d),end="")
        d += 1
    print()
