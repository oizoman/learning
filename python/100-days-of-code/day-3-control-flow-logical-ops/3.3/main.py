# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Divisible by 4 and evenly divisible by 100 and also 400, LEAP YEAR.")
        else:
            print("Divisible by 4 and evenly divisible by 100 but not 400, NOT A LEAP YEAR.")
    else:
        print("Divisible by 4 and not evenly divisible by 100, LEAP YEAR.")
else:
    print("Not divisible by 4, NOT A LEAP YEAR.")