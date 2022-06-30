import random

from numpy import append
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
easy_pass = ""

for letter in range(0, nr_letters):
    easy_pass+=letters[round(int(random.random()*len(letters)))]

for number in range(0, nr_numbers):
    easy_pass+=numbers[round(int(random.random()*len(numbers)))]

for symbol in range(0, nr_symbols):
    easy_pass+=symbols[round(int(random.random()*len(symbols)))]

print(f"Easypass is {easy_pass}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
hard_pass = ""

letters_left = nr_letters
numbers_left = nr_numbers
symbols_left = nr_symbols

while(letters_left > 0 or numbers_left > 0 or symbols_left > 0):
    next_char = random.randint(0,2)
    if (next_char == 0 and letters_left > 0):
        print("Letter selected, Subtracting 1")
        hard_pass+=letters[round(int(random.random()*len(letters)))]
        letters_left-=1
    elif (next_char == 1 and numbers_left > 0):
        print("Number selected, Subtracting 1")
        hard_pass+=numbers[round(int(random.random()*len(numbers)))]
        numbers_left-=1
    elif (next_char == 2 and symbols_left > 0):
        print("Symbol selected, Subtracting 1")
        hard_pass+=symbols[round(int(random.random()*len(symbols)))]
        symbols_left-=1
    else:
        print("Nothing added to hardpass this iteration")
    
    
    print(f"Letters left - {letters_left}")
    print(f"Numbers left - {numbers_left}")
    print(f"Symbols left - {symbols_left}")


print(f"Hardpass is {hard_pass}")
