from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
time = ''
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    title.config(text='Timer', fg=GREEN)
    checkmark.config(text='')
    start.config(text='Start')
    global reps
    reps = 0


# ---------------------------- TIMER STOP ------------------------------- #

def stop_timer():
    window.after_cancel(timer)
    global time
    time = canvas.itemcget(timer_text, 'text')
    start.config(text="Play")
    if start['text'] == 'Play':
        start.config(command=play_timer)


# ---------------------------- TIMER PLAY ------------------------------- #

def play_timer():
    global time
    time_comp = time.split(':')
    count = int(time_comp[0]) * 60 + int(time_comp[1])
    countdown(int(count))
    start.config(text="Stop")
    if start['text'] == 'Stop':
        start.config(command=stop_timer)


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    start.config(text='Stop', command=stop_timer)
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        title.config(text='Long Break', fg=RED)
        countdown(long_break_sec)

    elif reps % 2 == 0:
        title.config(text='Short Break', fg=PINK)
        countdown(short_break_sec)

    else:
        title.config(text='Work', fg=GREEN)
        countdown(work_sec)
        mark = ''
        for i in range(math.floor(reps / 2)):
            mark += '✔'
        checkmark.config(text=mark)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):
    minute = math.floor(count/60)
    sec = count % 60
    if sec < 10:
        sec = '0' + str(sec)
    canvas.itemconfig(timer_text, text=f"{minute}:{sec}")

    if count > 0:
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("POMODORO")
window.minsize(width=600, height=400)
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=300, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file='tomato.png')
canvas.create_image(150, 112, image=tomato)
timer_text = canvas.create_text(150, 140, text='00:00', fill='white', font=(FONT_NAME, 30, 'bold'))
canvas.grid(column=1, row=2)

title = Label(text='Timer')
title.config(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, 'bold'))
title.grid(column=1, row=0)

start = Button(text='Start', command=start_timer, font=(FONT_NAME, 15, 'normal'))
start.config(highlightthickness=0, bg=GREEN, padx=20, pady=5, border=2)
start.grid(column=0, row=4)

reset = Button(text='Reset', command=reset_timer, font=(FONT_NAME, 15, 'normal'))
reset.config(highlightthickness=0, bg=RED, padx=20, pady=5, border=2)
reset.grid(column=2, row=4)

checkmark = Label()
checkmark.config(fg=GREEN, bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 30, 'bold'))
checkmark.grid(column=1, row=3)

window.mainloop()
