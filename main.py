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

todo_sit = "work"
# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start():
	print("a")


def reset():
	print("a")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
mechanism = []

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("pomodoro")
window.minsize(600, 500)

todo_label = Label(text=todo_sit, font=("Arial", 30, "normal"))
todo_label.place(x=0, y=0)

canvas = Canvas(width=200, height=224)
tomato_src = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_src)
canvas.place(column=1, row=1)
start_button = Button(text="start", border=10, command=start)
reset_button = Button(text="reset", border=10, command=reset)

window.mainloop()
