import random

game = True

while(game):
    user_choice = int(input("Type 0 for ROCK, 1 for PAPER or 2 for SCISSORS. \n"))
    if user_choice < 0 or user_choice > 2 or type(user_choice) != int:
        continue
    machine_choice = random.randint(0,2)
    if(user_choice == 0 and machine_choice == 0 or user_choice == 1 and machine_choice == 1 or user_choice == 2 and machine_choice == 2):
        print("Tie\n")
    elif(user_choice == 0 and machine_choice == 1 or user_choice == 1 and machine_choice == 2 or user_choice == 2 and machine_choice == 0):
        print("You Lost!\n")
        print(f"{machine_choice}")
        game = False
    else:
        print("You won!")
        print(f"{machine_choice}")

        game = False
    
