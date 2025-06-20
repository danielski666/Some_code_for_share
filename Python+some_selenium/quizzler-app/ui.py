import tkinter

THEME_COLOR = "#375362"

from tkinter import *
from quiz_brain import QuizBrain


class QuizInterface():

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("QuizzlerAPP")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_lbl = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 12, "normal"))
        self.score_lbl.grid(row=0, column=1)

        self.canvas = Canvas(bg="white", width=300, height=250)
        self.q_text = self.canvas.create_text(150, 125, text="Question text.",
                                              font=("Arial", 20, "italic"), fill=THEME_COLOR,
                                              width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        img_t = PhotoImage(file="images/true.png")
        self.true_button = Button(image=img_t, highlightthickness=0, command=self.true_button_pressed)
        self.true_button.grid(row=2, column=0)

        img_f = PhotoImage(file="images/false.png")
        self.false_button = Button(image=img_f, highlightthickness=0, command=self.false_button_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_lbl.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.q_text, text=q_text)
        else:
            self.canvas.itemconfig(self.q_text, text="You have reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_button_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))


    def false_button_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))


    def give_feedback(self, is_correct):
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)