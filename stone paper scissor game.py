
import random

choices = ["rock", "paper", "scissors"]

user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
computer_choice = random.choice(choices)

print(f"You chose {user_choice}, and the computer chose {computer_choice}.\n")

if user_choice == computer_choice:
    result = "It's a tie!"
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "paper" and computer_choice == "rock") or \
     (user_choice == "scissors" and computer_choice == "paper"):
    result = f"{user_choice.capitalize()} wins!"
else:
    result = f"{computer_choice.capitalize()} wins!"

print(result)