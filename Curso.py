import tkinter as tk

class Questionnaire(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.question_label = tk.Label(self, text="Qual é a capital do Brasil?")
        self.question_label.pack()

        self.answer_entry = tk.Entry(self)
        self.answer_entry.pack()

        self.submit_button = tk.Button(self, text="Enviar", command=self.check_answer)
        self.submit_button.pack()

        self.result_label = tk.Label(self, text="")
        self.result_label.pack()

    def check_answer(self):
        answer = self.answer_entry.get()
        if answer.lower() == "brasília":
            self.result_label.config(text="Correto!")
        else:
            self.result_label.config(text="Incorreto.")

root = tk.Tk()
app = Questionnaire(master=root)
app.mainloop()
