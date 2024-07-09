import random

options = ["rock","paper","scisor"]

computer_score = 0
your_score = 0

while True:
    user_choice = input("please enter your choice from rock\paper\scisor or q for quit the game \n").lower()
    
    if user_choice == "q":
        break
    
    elif user_choice in options:
        
    
        random_index = random.randint(0,2)
        computer_choice = options[random_index]
    
        if user_choice == "rock" and computer_choice == "scisor":
            print("you won")
            your_score += 1
            print(computer_choice)
        
        elif user_choice == "paper" and computer_choice == "rock":
            print("you won")
            your_score += 1
            print(computer_choice)
        
        elif user_choice == "scisor" and computer_choice == "paper":
            print("you won")
            your_score += 1
            print(computer_choice)
        
        else:
            print("you lose")
            computer_score += 1
            print(computer_choice)
        
print("thank for playing with me")
print(your_score,"\n", computer_score)
    