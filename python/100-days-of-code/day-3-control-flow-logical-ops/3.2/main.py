# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = int(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = int(weight//(height**2))

print(f"BMI = {weight} / {height}^2 = {bmi}")

if bmi <= 18.5:
    print("You are underweight.")
elif 18.5 < bmi <= 25:
    print("You are normal weight.")
elif 25 < bmi <= 30:
    print("You are overweight.")
elif 30 < bmi <= 35:
    print("You are obese.") 
elif bmi > 35:
    print("You are morbidly obese.")
