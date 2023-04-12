import random

def get_choice():
    player_choice = input("Enter a choice (rock, paper, scissors) :")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f"You chose {player}, Computer chose {computer}")
    if player == computer:
        return("Tt's a tie")
    elif player == "rock":
        if computer == "scissors":
            return("rock smashes the scissors You win!")
        else:
            return("Paper got the rock! Sorry computer won")
    elif player == "scissors":
        if computer == "rock":
            return ("Rock gets the scissors and You lost")
        else:
            return("Scissors cuts the paper and You won")
    elif player == "paper":
        if computer == "rock":
            return("Paper gets the rock and You won")
        else:
            return("Scissors cuts the paper and you lost")

def play():
    choices = get_choice()
    results = check_win(choices["player"], choices["computer"])
    print(results)


play()
