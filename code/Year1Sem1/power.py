def power(x, n):
    result = 1
    for i in range (n):
        result = result * x
    return result

base = int(input("Please enter the base : "))
exp = int(input("Please enter the exponent : "))

answer = power(base,exp)
print('the answer is',answer)