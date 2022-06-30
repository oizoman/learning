# print(round(2.6666666, 2))

# print(8//3)

# score = 100
# height = 1.2
# isWinning = True
# #f-string
# print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}")

# 🚨 Don't change the code below 👇
age = int(input("What is your current age?"))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
years_left = 90 - age

days_left = years_left * 365
weeks_left = years_left * 52
months_left = years_left * 12

print(f"You have: \n{days_left} days left, or\n{weeks_left} weeks left, or\n{months_left} months left.\nHave a nice life!")
