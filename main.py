from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# ------------------ Reading CSV File ------------------- #
data = pandas.read_csv("data/french_words.csv")
french_word_list = data["French"].to_list()
print(random.choice(french_word_list))

# ------------------ UI --------------------------------- #
canvas = Canvas(width=800,height=526)
card_front = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
title_text = canvas.create_text(400, 150, text="Title",  font=("Ariel",40,"italic"))
word_text = canvas.create_text(400, 263, text="WORD",  font=("Ariel",60,"bold"))
canvas.grid(column=0, row=0, columnspan=2)

#Buttons
right_image = PhotoImage(file="images/right.png")
right_image_button = Button(image=right_image, highlightthickness=0)
right_image_button.grid(column=1,row=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_image_button = Button(image=wrong_image, highlightthickness=0)
wrong_image_button.grid(column=0,row=2)


window.mainloop()
