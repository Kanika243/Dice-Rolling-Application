from tkinter import *
import random

# Initialize the main window
root = Tk()
root.geometry("700x450")
root.title("Roll Dice")

root.configure(bg="purple")

# Create a label to display the dice result
label = Label(root, text="", font=("times", 200), bg="lightblue")
label.pack(pady=20)  

def roll():
    # Dice symbols
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    # Update the label with two random dice rolls
    label.configure(text=f'{random.choice(dice)} {random.choice(dice)}')

# Create a button to roll the dice
button = Button(root, text="Let's Roll!", width=40, height=6, font=10, bg="pink", bd=2, command=roll)
button.pack(padx=10, pady=10)

root.mainloop()






