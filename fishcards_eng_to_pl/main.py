from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
from pathlib import Path
import pandas
import pyperclip
import json
import random
import pandas as pd

learning_file = Path("have_to_learn.csv")
if learning_file.is_file():
    df = pd.read_csv("have_to_learn.csv", encoding='windows-1250')
    df_dict = {row.English: row.Polish for (index, row) in df.iterrows()}
else:
    df = pd.read_csv("data/polisf_words.csv", encoding='windows-1250')
    df_dict = {row.English: row.Polish for (index, row) in df.iterrows()}

temp_dict = []


def remove_word():
    print(temp_dict)
    try:
        for k in temp_dict:
            if k in df_dict.keys():
                del df_dict[k]
                temp_dict.remove(k)
                generate_english()
            elif bool(df_dict) == False:
                canvas.itemconfig(title, text="Bravo you learned everything !", fill="black")
                canvas.itemconfig(random_word, text="", fill="black")
    except IndexError:
            canvas.itemconfig(title, text="Bravo you learned everything !", fill="black")
            canvas.itemconfig(random_word, text="", fill="black")


def have_to_learn():
    new_dict = {key: value for k in temp_dict for key, value in df_dict.items() if key == k}
    labels = ["English", "Polish"]
    data = pd.DataFrame(new_dict.items())
    data.columns = labels
    data.to_csv("have_to_learn.csv", index=False)
    generate_english()


def generate_english():
    global flip_timer
    window.after_cancel(flip_timer)
    random_english = random.choice(list(df_dict.keys()))
    temp_dict.append(random_english)
    canvas.itemconfig(title, text="English", fill="black")
    canvas.itemconfig(random_word, text=random_english, fill="black")
    canvas.itemconfig(canvas_image, image=card_front)
    flip_timer = window.after(4000, change_card)



def generate_polish():
    polish_word = canvas.itemcget(random_word, 'text')
    canvas.itemconfig(title, text="Polish", fill="white")
    for key, value in df_dict.items():
        if key == polish_word:
            canvas.itemconfig(random_word, text=value, fill="white")


def change_card():
    generate_polish()
    canvas.itemconfig(canvas_image, image=card_back)

# UI

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(4000, change_card)

canvas = Canvas(width=800, height=526, highlightthickness=0)
canvas.configure(bg=BACKGROUND_COLOR)
card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=card_front)
title = canvas.create_text(400, 150, text="E", font=("Ariel", 40, "italic"))
random_word = canvas.create_text(400, 263, text="test", font=("Ariel", 50, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
cancel_image = PhotoImage(file="images/wrong.png")
approved_image = PhotoImage(file="images/right.png")
canceled_button = Button(image=cancel_image, highlightthickness=0, command=have_to_learn)
canceled_button.grid(row=1, column=0)
approved_button = Button(image=approved_image, highlightthickness=0, command=remove_word)
approved_button.grid(row=1, column=1)

generate_english()
window.mainloop()