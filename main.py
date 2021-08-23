import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.25
SHORT_BREAK_MIN = 0.05
LONG_BREAK_MIN = 0.20
reps = 0
check = ""
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text,text="00:00")
    check_label["text"] = ""
    global  reps,check
    reps = 0
    check = "None"


# ---------------------------- TIMER MECHANISM ------------------------------- #


def click():
    global reps
    global check
    reps += 1
    worksec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if reps <= 8:
        if reps % 8 == 0:
            cut_down(long_break)
            timer_label.config(text="Long break", fg=GREEN)
        elif reps % 2 == 0:
            cut_down(short_break)
            timer_label.config(text="short break", fg=PINK)
        else:
            cut_down(worksec)
            timer_label.config(text="Work", fg=RED)

            check_label.config(text=check)
            check += "✔"






# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def cut_down(count):
    global timer
    minutes = math.floor(count/60)
    seconds = count % 60
    if seconds < 10:
        seconds = "0" + f"{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        timer = window.after(1000, cut_down, count - 1)
    else:
        click()

# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
# colorhunt.co可以寻觅16进制颜色
# canvas也是tinker中类似label等的Widget,都有text,bg等属性
canvas = tkinter.Canvas(width=202, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=tomato_img)
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

timer_label = tkinter.Label(text="Timer", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid(column=1, row=0)

start_button = tkinter.Button(text="Start", bg="#FFFFFF",command=click)
start_button.grid(column=0, row=2)
reset_button = tkinter.Button(text="Reset", bg="#FFFFFF", command=reset)
reset_button.grid(column=2, row=2)

check_label = tkinter.Label(text=check, bg= YELLOW,fg=GREEN)
check_label.grid(column=1, row=3)


window.mainloop()   # ms级更新
