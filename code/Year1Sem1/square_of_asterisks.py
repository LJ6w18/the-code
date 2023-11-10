def print_char(char, n):
    for i in range(n):
        print(char, end=" ")

def print_square(size):
    for i in range(size):
        print_char("*", size)
        print()

size = int(input("Enter the number of rows: "))
print_square(size)