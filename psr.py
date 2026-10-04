from tkinter import *
import random

window = Tk()
window.title("Rock, Paper, Scissors Game")
window.geometry("600x600")
window.config(bg="light blue")

# Text label
result_label = Label(window, text="Choose rock, paper, or scissors.")
result_label.pack(pady=20)


def play(choice):

    #Randomly chooses aout of r,p, or s
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    #Result for each possibility
    if choice == computer_choice:
        result = "It's a tie!"

    elif choice == "Rock" and computer_choice == "Scissors":
        result = "You win!"

    elif choice == "paper" and computer_choice == "Scissors":
        result = "Computer wins! Better luck next time."

    elif choice == "Scissors" and computer_choice == "Paper":
        result = "You win!"

    else:
        result = "Computer wins! Better luck next time."

    #Displays the text based on choice
    result_label.config(
        text="You chose " + choice +
        "\nComputer chose " + computer_choice +
        "\n\n" + result
    )

#Functions for each option
def rock():
    play("Rock")


def scissors():
    play("Scissors")


def paper():
    play("Paper")

#Rock button
rock_button = Button(window,text="Rock",command=rock,bg="light blue")
rock_button.pack(pady=10)

#Scissors button
scissors_button = Button(window, text="Scissors",command=scissors,bg="light blue")
scissors_button.pack(pady=10)

#Paper button
paper_button = Button(window,text="Paper",command=paper,bg="light blue")
paper_button.pack(pady=10)


window.mainloop()