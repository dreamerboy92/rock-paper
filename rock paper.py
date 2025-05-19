"""
workflow of project:
input from user(rock, paper, scissor)
computer choice (computer will choose randomly not conditionally)
result print

cases:
A- Rock
Rock - Rock = tie
Rock - paper = paper win
rock - scissor = rock wine

B - paper
paper - paper = tie
paper - rock = paper win
paper - scissor = scissor win

C -scissor
 scissor - scissor = tie
 scissor - rock = rock win
 scissor- paper = sc issor win


"""

import random 
item_list = ["Rock", "Paper","Scissor"]

user_choice = input("Enter your move = Rock, Paper , Scissor =")
comp_choice = random.choice(item_list)

print(f"User choice = {user_choice}, Computer choice = {comp_choice}")

if user_choice == comp_choice:
    print("Both chooses same: = Match tie")

elif user_choice == "Rock":
    if comp_choice == "Paper":
         print("Paper covers Rock = Computer")
    else:
        print("Rock smashes Scissor = You win")

elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("Scissor cuts paper, Computer win")
    else:
        print("Paper covers rock, you win")
elif user_choice == "Scissor":
    if comp_choice == "Paper";
        print("Scissot cuts paper, Computer win")
    else:
        print("Rock smashes scissor, computer win")
        