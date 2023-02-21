import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
check = '✓'
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    window.after_cancel(timer)
    label.config(text="TIMER", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    checker.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        label.config(text='Break', fg=RED)
        count_down(LONG_BREAK_MIN*60)
    elif reps % 2 == 0:
        label.config(text='Break', fg=PINK)
        count_down(SHORT_BREAK_MIN*60)
    else:
        label.config(text='Work', fg=GREEN)
        count_down(WORK_MIN*60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(num):
    global reps
    mins = math.floor(num/60)
    sec = num % 60
    if sec < 10:
        sec = "0"+f"{sec}"
    canvas.itemconfig(timer_text, text=f"{mins}:{sec}")
    if num > 0:
        global timer
        timer = window.after(1000, count_down, num-1)
    else:
        start_timer()
        if reps % 2 == 0:
            checker['text'] += check


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=('courier', 35, 'bold'))
canvas.grid(column=1, row=1)

start = Button(text='START', highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)

reset = Button(text='RESET', highlightthickness=0, command=reset_timer)
reset.grid(column=2, row=2)

label = Label(text="TIMER", fg=GREEN, font=('courier', 55, 'bold'), bg=YELLOW)
label.grid(column=1, row=0)

checker = Label(fg=GREEN, font=('courier', 35, 'bold'), bg=YELLOW)
checker.grid(column=1, row=3)

window.mainloop()
