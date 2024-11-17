"""
WORKFLOW OF PROJECT:
1- Input from user(Rock, paper, scissor)
2- Computer choice (Computer will choose randomly not conditionally)
3- Result print

Cases:
A- Rock
Rock - Rock = tie
Rock - Paper = Paper win
Rock - scissor = Rock win

B- Paper
Paper - Paper = tie
Paper - Rock = Paper win
Paper - Scissor = Scissor win

C- Scissor
Scissor - Scissor = tie
Scissor - Rock = Rock win
Scissor - Paper = Scissor win
"""

import random
item_list = ["Rock", "Paper", "Scissor"]

user_choice = input("Enter your move = Rock, Paper or Scissor: ")
comp_choice = random.choice(item_list)
print(f"user_choice: {user_choice}, comp_choice: {comp_choice}")

if user_choice == comp_choice:
    print("both chooses the Same : Match tie ")

elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper cover the rock, Computer win")
    else:
        print("Rock smashes scissor, You win")

elif user_choice == "Paper":
    if comp_choice == "Rock":
        print("Paper cover the rock, You win")
    else:
        print("Scissor cut the Paper, Computer win")

elif user_choice == "Scissor":
    if comp_choice == "Rock":
        print("Rock smashes the scissor, Computer win")
    else:
        print("Scissor cut the Paper, You win")