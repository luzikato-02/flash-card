import random
import pandas
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# Read csv file and convert to dictionary
# data = pandas.read_csv('data/french_words.csv')
# to_learn = data.to_dict(orient='records')

try:
    data = pandas.read_csv('words_to_learn.csv')
except FileNotFoundError:
    data = pandas.read_csv('data/french_words.csv')
    to_learn = data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')

def next_card():
    # Globalize variables
    global current_card, flip_timer
    # Stop timer until redefined again
    window.after_cancel(flip_timer)
    # Get word from data
    current_card = random.choice(to_learn)
    french_word = current_card['French']
    # Change background image
    canvas.itemconfig(card_background, image=front_img)
    # Change text color
    canvas.itemconfigure(card_title, text='French', fill='black')
    canvas.itemconfigure(card_word, text=french_word, fill='black')
    # Redefine timer with 3s delay and run 'flip_card' function
    flip_timer = window.after(3000, flip_card)

def flip_card():
    # Get english word from global variabel
    english_word = current_card['English']
    # Change background image
    canvas.itemconfig(card_background, image=back_img)
    # Change text color
    canvas.itemconfigure(card_title, text='English', fill='white')
    canvas.itemconfigure(card_word, text=english_word, fill='white')

def word_known():
    if current_card in to_learn:
        to_learn.remove(current_card)
        new_data = pandas.DataFrame(to_learn)
        new_data.to_csv("words_to_learn.csv", index=False)
    next_card()


# Setup tkinter window
window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Define timer as a variable for easier use
flip_timer = window.after(3000, flip_card)

# Setup canvas and load images
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
check_image = PhotoImage(file='images/right.png')
cross_image = PhotoImage(file='images/wrong.png')
front_img = PhotoImage(file='images/card_front.png')
back_img = PhotoImage(file='images/card_back.png')

# Setup images and text
card_background = canvas.create_image(400, 263, image=front_img)
card_title = canvas.create_text(400, 150, text="", font=('Ariel', 40, 'italic'))
card_word = canvas.create_text(400, 263, text="", font=('Ariel', 60, 'bold'))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
know_button = Button(image=check_image, highlightthickness=0, command=word_known)
know_button.grid(column=1, row=1)
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

# Get data after window and widgets loaded
next_card()





















window.mainloop()
