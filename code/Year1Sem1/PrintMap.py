map =	[ ['T', ' ', ' ', ' ', 'T'],\
          [' ', 'P', ' ', ' ', ' '],\
          [' ', ' ', ' ', 'T', ' '],\
          [' ', 'T', ' ', ' ', ' ']]
num_row = len(map)
num_column = len(map)
for column in range(num_column):
    print("+----",end = '')
print("+")

for row in range(num_row):
    for column in map[row]:
        print("| {} ".format(column),end="")
    print("|")

    for column in range(num_column):
        print("+----",end = '')
    print("+")

    