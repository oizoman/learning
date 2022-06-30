#1. Create a greeting for your program.
from unicodedata import name


print("Hi from <BAND NAME GENERATOR>")

#2. Ask the user for the city that they grew up in.
city_of_birth = input("Which city did you grow up in?\n")

#3. Ask the user for the name of a pet.
name_of_pet = input("What's the name of your pet?\n")

#4. Combine the name of their city and pet and show them their band name.
print("Your band name is: The " + city_of_birth + " " + name_of_pet + "s")

#5. Make sure the input cursor shows on a new line, see the example at:
#   https://replit.com/@appbrewery/band-name-generator-end