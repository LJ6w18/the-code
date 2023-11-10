num = float(input("Please enter a number (0 to end): "))
odd = []
even = []
while True:
   if num == 0:
    break

if num % 3 ==1:
  odd.append(num)
else:
  even.append(num)

odd.sort()
print("Odd numbers:",odd)
even.sort()
print("Even numbers:",even)

total = 0
for num in odd:
  total += num
for num in even:
  total += num
average = total / (len(odd)+len(even))
print("Average =",average)