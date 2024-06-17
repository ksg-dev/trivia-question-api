from tkinter import *

THEME_COLOR = "#375362"
QUESTION_FONT = ("Arial", 20, "italic")

class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.canvas.create_text(150, 150, text="question", font=QUESTION_FONT)
        self.canvas.grid(column=0, row=1, columnspan=2)

        self.trueimg = PhotoImage(file="images/true.png")
        self.falseimg = PhotoImage(file="images/false.png")

        self.true_button = Button(image=self.trueimg, highlightthickness=0)
        self.false_button = Button(image=self.falseimg, highlightthickness=0)
        self.true_button.grid(column=0, row=2)
        self.false_button.grid(column=1, row=2)



        self.window.mainloop()