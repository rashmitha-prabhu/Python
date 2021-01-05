from tkinter import *
import pandas
import random
import time
BACKGROUND_COLOR = "#B1DDC6"
word = {}


# ------------------ READ CSV ------------------
try:
    data = pandas.read_csv('data/words_to_learn.csv')
    if data.empty:
        data = pandas.read_csv('data/french_words.csv')
except pandas.errors.EmptyDataError:
    data = pandas.read_csv('data/french_words.csv')
    to_learn = data.to_dict(orient='records')
except FileNotFoundError:
    data = pandas.read_csv('data/french_words.csv')
    to_learn = data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')


# ------------------ RANDOM WORDS ------------------
def get_word():
    global word, flip_timer
    window.after_cancel(flip_timer)
    try:
        word = random.choice(to_learn)
    except IndexError:
        canvas.itemconfig(card_title, text='', fill='black')
        canvas.itemconfig(card_word, text='COMPLETE', fill='black')
    else:
        canvas.itemconfig(card, image=card_front)
        canvas.itemconfig(card_title, text='French', fill='black')
        canvas.itemconfig(card_word, text=word['French'], fill='black')
        flip_timer = window.after(3000, card_flip)


# ------------------ FLIP CARD ------------------
def card_flip():
    canvas.itemconfig(card, image=card_back)
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=word['English'], fill='white')


# ------------------ KNOWN WORDS ------------------
def is_known():
    try:
        to_learn.remove(word)
    except ValueError:
        pass
    else:
        get_word()
    finally:
        new_data = pandas.DataFrame(to_learn)
        new_data.to_csv("data/words_to_learn.csv", index=False)


# ------------------ USER INTERFACE ------------------
window = Tk()
window.title("FLASHY")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, card_flip)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front = PhotoImage(file='images/card_front.png')
card_back = PhotoImage(file='images/card_back.png')
card = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, font="Ariel 40 italic")
card_word = canvas.create_text(400, 263, font="Ariel 60 bold")
canvas.grid(row=0, column=0, columnspan=2)

wrong_img = PhotoImage(file='images/wrong.png')
wrong = Button(image=wrong_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=get_word)
wrong.grid(row=1, column=0)

right_img = PhotoImage(file='images/right.png')
right = Button(image=right_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=is_known)
right.grid(row=1, column=1)

get_word()

window.mainloop()
