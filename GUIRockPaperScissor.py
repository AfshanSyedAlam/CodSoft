import tkinter as tk
import random

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game(player_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    result = determine_winner(player_choice, computer_choice)
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")

window = tk.Tk()
window.title("Rock, Paper, Scissors Game")

title_label = tk.Label(window, text="Rock, Paper, Scissors", font=("Helvetica", 20))
title_label.pack()

result_label = tk.Label(window, text="", font=("Helvetica", 16))
result_label.pack()

rock_button = tk.Button(window, text="Rock", command=lambda: play_game("Rock"))
rock_button.pack(side="left")

paper_button = tk.Button(window, text="Paper", command=lambda: play_game("Paper"))
paper_button.pack(side="left")

scissors_button = tk.Button(window, text="Scissors", command=lambda: play_game("Scissors"))
scissors_button.pack(side="left")

exit_button = tk.Button(window, text="Exit", command=window.quit, bg="red", fg="white")
exit_button.pack(side="right")

window.mainloop()
