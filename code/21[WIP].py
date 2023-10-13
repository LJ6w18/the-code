import random
card1 = int(input("Enter card 1:"))
card2 = int(input("Enter card 2:"))
card3 = int(input("Enter card 3:"))
if card1 >10:
    card1 = 10
if card2 >10:
    card2 =10
if card3 >10:
    card3 =10
a = card1+card2+card3
if card1 == 1:
    a += 10
    if a >21:
        a -= 10
if card2 == 1:
    a += 10
    if a >21:
        a -= 10
if card3 == 1:
    a += 10
    if a >21:
        a -= 10
print("total value =",a)  

