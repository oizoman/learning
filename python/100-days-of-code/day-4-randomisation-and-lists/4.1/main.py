import random
# import my_module

# print(random.randint(0,333))
# print(my_module.pi)

# print(random.random())

#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲

for x in range(10):
    outcome = random.randint(0,1)
    if(outcome==0):
        print("Heads.")
    else:
        print("Tails.")