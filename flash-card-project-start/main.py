from tkinter import *
import pandas
import random
import os

BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}


try:
    data_file = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data_file.to_dict(orient="records")


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    print(len(to_learn))
    next_card()


def reset():
    global original_data, to_learn
    if os.path.exists("data/words_to_learn.csv"):
        os.remove("data/words_to_learn.csv")
        original_data = pandas.read_csv("data/french_words.csv")
        to_learn = original_data.to_dict(orient="records")
    else:
        print("The File does not exist.")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(canvas_image, image=front_image)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image=back_image)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Front Image
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=front_image)
card_title = canvas.create_text(400, 150, text="Title", fill="Black", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", fill="Black", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Back Image
back_image = PhotoImage(file="images/card_back.png")


# Button
right_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

reset_button = Button(text="Reset", highlightthickness=0, command=reset)
reset_button.grid(row=1, column=2)

next_card()

window.mainloop()

