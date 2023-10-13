a = input("Enter a Character:")
b = int(input("Enter a number:"))

for level in range (b):
    start_pos = b - level - 1
    
    for i in range (start_pos):
        print(" ", end = "")

    for i in range (level + 1):
        print(a, end = " ")
    print()

print("Merry Christmas!")