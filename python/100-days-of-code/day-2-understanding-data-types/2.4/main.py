#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to <TIP CALCULATOR>")
total_bill = float(input("What was the total bill? - $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? - "))
party_size = int(input("How many people are splitting the bill? - "))

final_contribution = float(total_bill + (total_bill/100)*tip_percentage) / party_size


print("Each person should pay: $" + str(round(final_contribution, 2)))