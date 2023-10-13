def print_char(char, size):
    for i in range(size):
        for j in range(size):
            print(char, end=" ")
        print()

size = int(input("Please tell us how big you want your square to be: "))
char = input("What character do you want it to be formed with? ")
print_char(char, size)
