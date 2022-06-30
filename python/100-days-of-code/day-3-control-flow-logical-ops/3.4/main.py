# 🚨 Don't change the code below 👇
from typing import final


print("\nWelcome to Python Pizza Deliveries!")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
final_bill = 0

while True:
    size = input("\nWhat size pizza do you want? S, M, or L?\n")
    if size == "S":
        final_bill+=15
        break
    elif size == "M":
        final_bill+=20
        break
    elif size == "L":
        final_bill+=25
        break
    else:
        print("INVALID ENTRY")

while True:
    add_pepperoni = input("\nDo you want pepperoni? Y or N?\n")
    if add_pepperoni == "Y":
        if size == "S":
            final_bill +=2
            break
        else:
            final_bill+=3
            break
    elif add_pepperoni == "N":
        break
    else:
        print("INVALID ENTRY")


while True:
    extra_cheese = input("\nDo you want extra cheese? Y or N?\n")
    if add_pepperoni == "Y":
        final_bill+=1
        break
    elif add_pepperoni == "N":
        break
    else:
        print("INVALID ENTRY")


print(f"\nFinal bill is ${final_bill}.\n")
