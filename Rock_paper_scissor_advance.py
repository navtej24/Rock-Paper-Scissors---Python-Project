import random

#define possible moves
moves=["rock","paper","scissor"]

def determine_winner(player, computer):
    if player == computer:
        return "Its is draw"
    elif (player == "rock" and computer == "scissor") or (player == "scissor" and computer == "paper") or (player == "paper" and computer == "rock"):
        return "You Win!"
    else:
        return "computer wins!"
    
while True:
    player_move = input("Enter your move from (rock, paper, scissor) :").lower()
    print(f"Player chose : {player_move}")

    # check for a valid move
    if player_move not in moves:
        print("Invalid move. Please try again")
        continue

    #check for a random move for computer
    computer_move = random.choice(moves)
    print(f"Computer chose : {computer_move}")

    #determine and display the winner
    result=determine_winner(player_move,computer_move)
    print(result)


    # options to play again
    play_again = input("Play Again?  yes or no : ").lower()
    if play_again != "yes":
        print("thanks for playing")
        print("------------------------------------------------------------")
        break