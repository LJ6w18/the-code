numbers = [2,7,11,6,7,3,17,7,12,41,8,11,13,10,15]
result = []
for value in numbers:
    if value%2 == 0:
        continue
    if value in result:
        continue
    result.append(value)
    if len(result) > 4:
        break
print(result)