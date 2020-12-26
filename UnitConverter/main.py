from tkinter import *


def convert():
    kms_output.delete(0, END)
    kms = float(mile_input.get()) * 1.609
    kms_output.insert(END, string=f"{kms}")


window = Tk()
window.title("Unit Converter")
window.config(padx=20, pady=20)

mile_input = Entry(width=15)
mile_input.insert(END, string='0')
mile_input.grid(column=1, row=0)

mile_label = Label(text=" miles", font=('Courier', 16, 'bold'))
mile_label.grid(column=2, row=0)

equals = Label(text=" is equal to ", font=('Courier', 16, 'bold'))
equals.grid(column=0, row=2)

kms_output = Entry(width=15)
kms_output.grid(column=1, row=2)

kms_label = Label(text=" km", font=('Courier', 16, 'bold'))
kms_label.grid(column=2, row=2)

button = Button(text='Calculate', command=convert)
button.grid(column=1, row=3)

window.mainloop()
