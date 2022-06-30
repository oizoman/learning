import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

player_points = 0
cpu_points = 0

rps_list = [rock, paper, scissors]

while True:
    player_choice = int(input("\nPlease enter 1 for Rock, 2 for Paper or 3 for scissors.\n"))-1
    cpu_choice = random.randint(0,2)

    if(player_choice == cpu_choice):
        print("~~~~~ DRAW ROUND ~~~~~")
    elif(player_choice == 0 and cpu_choice == 1):
        cpu_points+=1
    elif(player_choice == 1 and cpu_choice == 0):
        player_points+=1
    elif(player_choice == 2 and cpu_choice == 0): 
        cpu_points+=1
    elif(player_choice == 0 and cpu_choice == 2):
        player_points+=1
    elif(player_choice == 1 and cpu_choice == 2):
        cpu_points+=1
    elif(player_choice == 2 and cpu_choice == 1):
        player_points+=1
    else:
        print("\n<ERROR, YOU BROKE THE GAME>")
        break
    
    print("\n###### PLAYER CHOICE #####")
    print(rps_list[player_choice])
    print("\n###### CPU CHOICE #####")
    print(rps_list[cpu_choice])
    
    print(f"### PLAYER -\t {player_points}\n### CPU -\t {cpu_points}")

    if cpu_points == 3:
        print("\n##### GAME OVER, CPU WINS #####\n")
        break
    elif player_points == 3:
        print("\n##### YOU WIN! #####\n")
        break