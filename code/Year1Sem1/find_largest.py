def find_larger(n1,n2):
    if(n1 > n2):
        return n1
    else:
        return n2

n1=int(input("Enter the first interger number : "))

n2=int(input("Enter the second interger number : "))

n3=int(input("Enter the third interger number : "))

n4=int(input("Enter the fourth interger number : "))

larger1 = find_larger(n1,n2)

larger2 = find_larger(n3,n4)

larger = find_larger(larger1,larger2)

print("The largest interger is",larger)