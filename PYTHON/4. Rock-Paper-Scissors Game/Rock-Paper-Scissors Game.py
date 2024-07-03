import tkinter as tk
import random


user_score = 0
computer_score = 0

def play_game(user_choice):
    global user_score, computer_score
    
    
    choices = ['Rock', 'Paper', 'Scissors']
    user_choice_str = choices[user_choice]
    
    
    computer_choice = random.randint(0, 2)
    computer_choice_str = choices[computer_choice]
    
    
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        result = "You win!"
        user_score += 1
    else:
        result = "Computer wins!"
        computer_score += 1
    
    
    user_choice_label.config(text=f"Your choice: {user_choice_str}")
    computer_choice_label.config(text=f"Computer's choice: {computer_choice_str}")
    result_label.config(text=result)
    score_label.config(text=f"Score: You {user_score} - {computer_score} Computer")
    
def play_again():
    user_choice_label.config(text="Your choice: ")
    computer_choice_label.config(text="Computer's choice: ")
    result_label.config(text="")
    

root = tk.Tk()
root.title("Rock, Paper, Scissors Game")


user_choice_label = tk.Label(root, text="Your choice: ")
user_choice_label.pack()

rock_button = tk.Button(root, text="Rock", width=10, command=lambda: play_game(0))
rock_button.pack(pady=5)

paper_button = tk.Button(root, text="Paper", width=10, command=lambda: play_game(1))
paper_button.pack(pady=5)

scissors_button = tk.Button(root, text="Scissors", width=10, command=lambda: play_game(2))
scissors_button.pack(pady=5)

computer_choice_label = tk.Label(root, text="Computer's choice: ")
computer_choice_label.pack()

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

score_label = tk.Label(root, text="Score: You 0 - 0 Computer")
score_label.pack()

play_again_button = tk.Button(root, text="Play Again", command=play_again)
play_again_button.pack(pady=10)


root.mainloop()
