from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list += [random.choice(letters) for char in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for sym in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for num in range(random.randint(2, 4))]

    random.shuffle(password_list)

    p = ''.join(password_list)
    password_entry.insert(0, p)
    pyperclip.copy(p)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    web = website_entry.get()
    email = user_entry.get()
    p_word = password_entry.get()

    if len(web) == 0 or len(email) == 0 or len(p_word) == 0:
        messagebox.showwarning(title="OOPS", message="Please don't leave any fields empty")

    else:
        is_ok = messagebox.askokcancel(title='Check Details', message=f'Website: {web}\nEmail: {email}\n'
                                                                      f'Password: {p_word}\n\nProceed?')

        if is_ok:
            with open('data.txt', 'a') as file:
                file.write(f"{web} | {email} | {p_word}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50, bg='white')

canvas = Canvas(width=500, height=200, bg='white', highlightthickness=0)
logo = PhotoImage(file='logo.png')
canvas.create_image(250, 100, image=logo)
canvas.grid(column=0, row=0, columnspan=3)


# Labels
website = Label(text='Website:', bg='white', pady=10)
website.grid(column=0, row=1)

user = Label(text='Email/Username:', bg='white', pady=10)
user.grid(column=0, row=2)

password = Label(text='Password:', bg='white', pady=10)
password.grid(column=0, row=3)


# Entries
website_entry = Entry(width=45)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

user_entry = Entry(width=45)
user_entry.insert(0, 'sample@email.com')
user_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=24)
password_entry.grid(column=1, row=3)


# Buttons
generate_password = Button(text='Generate Password', highlightthickness=0, command=generate)
generate_password.grid(column=2, row=3)

add = Button(text='Add', width=42, highlightthickness=0, command=save)
add.grid(column=1, row=4, columnspan=3)

window.mainloop()
