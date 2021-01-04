from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


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


# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    web = website_entry.get().lower()
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title='ERROR', message='No Data File Found')
    else:
        try:
            messagebox.showinfo(title=web.title(), message=f'Email : {data[web.title()]["email"]}\nPassword : {data[web.title()]["password"]}')
        except KeyError:
            messagebox.showerror(title='ERROR', message='No details for the website exists')


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    web = website_entry.get().title()
    email = user_entry.get()
    p_word = password_entry.get()
    new_data = {
        web: {
            'email': email,
            'password': p_word,
        }
    }

    if len(web) == 0 or len(email) == 0 or len(p_word) == 0:
        messagebox.showwarning(title="OOPS", message="Please don't leave any fields empty")

    else:
        is_ok = messagebox.askokcancel(title='Check Details', message=f'Website: {web.title()}\nEmail: {email}\n'
                                                                      f'Password: {p_word}\n\nProceed?')
        if is_ok:
            try:
                with open('data.json', 'r') as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open('data.json', 'w') as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open('data.json', 'w') as file:
                    json.dump(data, file, indent=4)
            finally:
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
website_entry = Entry(width=24)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=1)

user_entry = Entry(width=45)
user_entry.insert(0, 'sample@email.com')
user_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=24)
password_entry.grid(column=1, row=3)


# Buttons
search = Button(text='Search', highlightthickness=0, command=find_password,  width=16)
search.grid(column=2, row=1)

generate_password = Button(text='Generate Password', highlightthickness=0, command=generate, width=16)
generate_password.grid(column=2, row=3)

add = Button(text='Add', width=42, highlightthickness=0, command=save)
add.grid(column=1, row=4, columnspan=3)

window.mainloop()
