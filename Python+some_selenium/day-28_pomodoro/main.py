import math
import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "🗸"
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    timer_label.config(text="Timer", foreground=GREEN, bg=YELLOW)
    canvas.itemconfig(timer_text, text="00:00")
    checkmark_label.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = 1#WORK_MIN * 60
    short_brake_sec =1# SHORT_BREAK_MIN * 60
    long_brake_sec = 5# LONG_BREAK_MIN * 60
    if reps == 9:
        return 0
    elif reps % 8 == 0:
        count_down(long_brake_sec)
        timer_label.config(text="Break", foreground=RED, bg=YELLOW)
    elif reps % 2 == 0:
        count_down(short_brake_sec)
        timer_label.config(text="Break", foreground=PINK, bg=YELLOW)
    else:
        timer_label.config(text="Work", foreground=GREEN, bg=YELLOW)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global reps, timer
    marks = ""
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        work_mark = math.floor(reps/2)
        for _ in range(work_mark):
            if reps % 8 != 0 and reps < 9:
                marks += CHECKMARK
        checkmark_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.config(padx=100, pady=50, bg=YELLOW)
window.title("Pomodoro")

canvas = tk.Canvas(width=200, height=234)
tomato_image = tk.PhotoImage(file="tomato.png")
canvas.config(bg=YELLOW, highlightthickness=0)  # instead of border = 0
canvas.create_image(100, 117, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

timer_label = tk.Label(font=(FONT_NAME, 50))
timer_label.config(text="Timer", foreground=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

checkmark_label = tk.Label(font=(FONT_NAME, 40, "bold"))
checkmark_label.config(foreground=GREEN, bg=YELLOW)
checkmark_label.grid(row=2, column=1)

start_button = tk.Button(text="Start", font=(FONT_NAME, 15), highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = tk.Button(text="Reset", font=(FONT_NAME, 15), command=reset_timer)
reset_button.grid(row=2, column=2)

window.mainloop()
