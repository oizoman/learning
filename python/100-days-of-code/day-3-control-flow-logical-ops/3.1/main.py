# condition = True

# if condition == 0:
#     print("Condition is false")
# elif condition == 1:
#     print("Condition is true")


# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
test_modulo = number % 2

if test_modulo == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")