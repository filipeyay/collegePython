import random

def get_choices():
    p_choice = input("Choose one (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    c_choice = random.choice(options)
    choices = { "player": p_choice, "computer": c_choice }
    return choices

def check_victory(player, computer):
    print(f"Player chose {player}, computer chose {computer}.")
    if player == computer:
        return "A tie!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! Victory!"
        else:
            return "Paper covers rock! You lose."
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! Victory!"
        else:
            return "Scissors cuts paper! You lose."
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cuts paper! Victory!"
        else:
            return "Rock smashes scissors! You lose."

choices = get_choices()
results = check_victory(choices["player"], choices["computer"])
print(results)
