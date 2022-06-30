# 🚨 Don't change the code below 👇
from itertools import count


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

total_score = 0

def count_true (name_a, name_b) :
    concat_name = (name_a + name_b).lower().replace(" ", "")
    
    method_count = 0

    method_count+=concat_name.count("t")
    method_count+=concat_name.count("r")
    method_count+=concat_name.count("u")
    method_count+=concat_name.count("e")

    print("True score is " + str(method_count))

    return method_count

def count_love (name_a, name_b) :
    concat_name = (name_a + name_b).lower().replace(" ", "")
    
    method_count = 0

    method_count+=concat_name.count("l")
    method_count+=concat_name.count("o")
    method_count+=concat_name.count("v")
    method_count+=concat_name.count("e")

    print("Love score is " + str(method_count))

    return method_count

true_score = str(count_true(name1,name2))
love_score = str(count_love(name1,name2))

total_score = true_score+love_score

if int(total_score) < 10:
    print(f"Your score is {total_score}, you go together like coke and mentos")
elif int(total_score) > 90:
    print(f"Your score is {total_score}, you go together like coke and mentos")
elif 40 <= int(total_score) < 50:
    print(f"Your score is {total_score}, you are alright together")
else:
    print(f"Your score is {total_score}, don't count on it")
