from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
current_data = {}
data = {}

try:
    whole_data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/data.csv")
    data = original_data.to_dict(orient="records")
else:
    data = whole_data.to_dict(orient="records")


def next_move():
    global current_data, timer
    screen.after_cancel(timer)
    current_data = choice(data)
    canvas.itemconfig(title_text, text="English", fill="black")
    canvas.itemconfig(word_text, text=current_data["English"], fill="black")
    canvas.itemconfig(background, image= front_photo)
    timer = screen.after(3000, func=flip_card)



def flip_card():
    canvas.itemconfig(title_text, text="Bangla", fill="white")
    canvas.itemconfig(word_text, text= current_data["Bangla"], fill="white", font= ("SolaimanLipi", 50, "bold"))
    canvas.itemconfig(background, image= back_photo)


def is_known():
    data.remove(current_data)
    unknown_data = pandas.DataFrame(data)
    unknown_data.to_csv("data/words_to_learn.csv", index=False)
    next_move()


screen = Tk()
screen.title("Translate")
screen.config(background=BACKGROUND_COLOR, padx=50, pady=50)

timer = screen.after(3000, func= flip_card)

canvas = Canvas(bg=BACKGROUND_COLOR, width=800, height=526, highlightthickness=0)
front_photo = PhotoImage(file="images/card_front.png")
back_photo = PhotoImage(file="images/card_back.png")
background = canvas.create_image(400, 263, image=front_photo)
title_text = canvas.create_text(400,150,text= "Title", font=("Arial", 30, "italic"))
word_text = canvas.create_text(400,263,text= "Word", font=("Arial", 50, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

dont_know_img = PhotoImage(file="images/wrong.png")
dont_know = Button(image=dont_know_img, highlightthickness=0, command= next_move)
dont_know.grid(row=1, column=0)

know_img = PhotoImage(file="images/right.png")
known = Button(image=know_img, highlightthickness=0, command= is_known)
known.grid(row=1, column=1)

next_move()

screen.mainloop()