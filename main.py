import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#FFF6BF"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0


# ---------------------------- TIMER RESET ------------------------------- #


# ---------------------------- TIMER MECHANISM ------------------------------- #

def reset():
    global reps
    reps = 0
    todo_label.config(text="Timer", font=("Courier", 40, "normal"))
    checkmark_canvas.delete("all")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("pomodoro")
window.minsize(600, 500)
window.config(bg="#FFF6BF", padx=100, pady=100)

todo_label = Label(text="Timer", bg="#FFF6BF", fg="#9bdeac", font=("Courier", 40, "normal"))
# todo_label.place(x=220, y=60)
todo_label.grid(column=1, row=0)

image_canvas = Canvas(width=200, height=224, highlightthickness=0)
tomato_src = PhotoImage(file="tomato.png")
image_canvas.config(bg="#FFF6BF")
image_canvas.create_image(100, 112, image=tomato_src)
timer_label = image_canvas.create_text(100, 130, text="00:00", font=("Courier", 20, "normal"), fill="white")
image_canvas.grid(column=1, row=1)

checkmark_canvas = Canvas(width=150, height=50, highlightthickness=0)
checkmark_canvas.grid(column=1, row=2)
checkmark_canvas.config(bg="#FFF6BF")


def count_down(count):
    global reps
    window.after(1000, count_down, count - 1)
    count_min = math.floor(count / 60)
    count_rest_sec = count % 60
    if count_min == 0:
        count_min = "00"
    if count_rest_sec < 10:
        count_rest_sec = f"0{count_rest_sec}"
    if count_rest_sec == 0:
        count_rest_sec = "00"
    if count >= 0:
        image_canvas.itemconfig(timer_label, text=f"{count_min}:{count_rest_sec}")
    elif count == -1:
        if reps < 4:
            reps = reps + 1
            image_canvas.itemconfig(timer_label, text=f"{SHORT_BREAK_MIN}:{count_rest_sec}")
            count_down(5*60)

            todo_label.config(text=f"{SHORT_BREAK_MIN} minutes rest", font=("Courier", 18, "normal"))
            checkmark_canvas.create_text(40 * reps, 20, text="ok", font=("Courier", 14, "normal"))
        elif reps == 4:
            todo_label.config(text=f"{LONG_BREAK_MIN} minutes rest", font=("Courier", 18, "normal"))


def start():
    todo_label.config(text="Work")
    count_down(5)


start_button = Button(text="start", border=3, command=start, padx=10, pady=10, font=("Courier", 15, "normal"))
start_button.grid(column=0, row=2)

reset_button = Button(text="reset", border=3, command=reset, padx=10, pady=10, font=("Courier", 15, "normal"))
reset_button.grid(column=2, row=2)


window.mainloop()
