from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# ------------------ Reading CSV File ------------------- #
data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)



def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


# ------------------ UI --------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer =  window.after(3000, func=flip_card)

french_word = random.choice(to_learn)
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
right_image = PhotoImage(file="images/right.png")
right_image_button = Button(image=right_image, highlightthickness=0, command=next_card)
right_image_button.grid(column=1, row=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_image_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_image_button.grid(column=0, row=2)

next_card()

window.mainloop()
