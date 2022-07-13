from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
learn = {}

# TODO read the data from the french_words.csv file in the data folder
try:
    data = pandas.read_csv("data/french_words.csv")
except FileNotFoundError:
    ori_data = pandas.read_csv("data/french_words.csv")
    print(ori_data)
    learn = ori_data.to.dict(orient="records")
else:
    learn = data.to_dict(orient="records")
curr_card = {}


def next_card():
    global curr_card, flip_timer
    windows.after_cancel(flip_timer)
    curr_card = random.choice(learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=curr_card["French"], fill="black")
    canvas.itemconfig(card_background, image=old_img)
    windows.after(3000, func=flip_card)
    flip_timer = windows.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=curr_card["English"], fill="white")
    canvas.itemconfig(card_background, image=new_image)


def is_known():
    learn.remove(curr_card)
    print(len(learn))
    data = pandas.DataFrame(learn)
    data.to_csv("data/words_to_learn.csv", index = False)
    next_card()


windows = Tk()
windows.title("flashy")
windows.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = windows.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
old_img = PhotoImage(file='images/card_front.png')
new_image = PhotoImage(file='images/card_back.png')
card_background = canvas.create_image(400, 263, image=old_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

card_title = canvas.create_text(400, 150, text="", fill="black", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", fill="black", font=("Ariel", 50, "bold"))

canvas.grid(row=0, column=0, columnspan=2)

c = PhotoImage(file='images/wrong.png')
unknown_but = Button(image=c, command=next_card,highlightthickness=0)
unknown_but.grid(column=0, row=1)


b = PhotoImage(file='images/right.png')
my_but = Button(image=b, command=is_known, highlightthickness=0)
my_but.grid(column=1, row=1)
my_but.config(padx=50, pady=50, highlightthickness=0)

next_card()

# data = pandas.read_csv("data/french_words.csv")
# print(data.to_dict)


windows.mainloop()
