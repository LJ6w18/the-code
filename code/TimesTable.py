num = int(input('Please enter a number: '))

for count in range(1,11):
    print('{:4} x {:<2} = {:<3}'.format(num,count,num*count))
print("The end.")