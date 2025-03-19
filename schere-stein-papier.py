import tkinter as tk
from tkinter import messagebox
import random


class RPSGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Rock Paper Scissors Game")
        self.window.geometry("400x300")
        self.window.resizable(False, False)
        self.window.configure(bg="#F3F3F3")
        self.window.protocol("WM_DELETE_WINDOW", self.quit_function)

        self.setup_widgets()

        self.random_RPS = ["Rock", "Paper", "Siccor"]

        self.score = 0
        self.computer_score = 0

    def setup_widgets(self):
        tk.Label(self.window, text="Rock Paper Siccor Game", font="Arial 12", bg="#F3F3F3").pack(pady=10)

        self.rock_btn = tk.Button(self.window, text="Rock", bg="lightblue", command=lambda: self.check_result("Rock"))
        self.paper_btn = tk.Button(self.window, text="Paper", bg="red", command=lambda: self.check_result("Paper"))
        self.siccor_btn = tk.Button(self.window, text="Siccor", bg="yellow", command=lambda: self.check_result("Siccor"))
        self.reset_btn = tk.Button(self.window, text="Reset", bg="purple", command=self.reset_function)

        self.your_score_label = tk.Label(self.window, text=f"Score: 0", font="Arial 11", bg="#F3F3F3")
        self.computer_score_label = tk.Label(self.window, text=f"Computer Score: 0", font="Arial 11", bg="#F3F3F3")

        self.rock_btn.place(x=110, y=55)
        self.paper_btn.place(x=175, y=55)
        self.siccor_btn.place(x=245, y=55)
        self.your_score_label.place(x=105, y=100)
        self.computer_score_label.place(x=105, y=120)
        self.reset_btn.place(x=175, y=160)

    def check_result(self, player_choice):
        computer_choice = random.choice(self.random_RPS)

        if computer_choice == player_choice:
            messagebox.showinfo("Result",
                                f"Your Choice: {player_choice} \nComputer Choice: {computer_choice} \nNo one Win")
        elif (computer_choice == "Rock" and player_choice == "Paper") or \
                (computer_choice == "Paper" and player_choice == "Siccor") or \
                (computer_choice == "Siccor" and player_choice == "Rock"):
            self.score += 1
            messagebox.showinfo("Result",
                                f"Your Choice: {player_choice} \nComputer Choice: {computer_choice} \nYou Win")
            self.your_score_label.config(text=f"Score: {self.score}")
        else:
            self.computer_score += 1
            messagebox.showinfo("Result",
                                f"Your Choice: {player_choice} \nComputer Choice: {computer_choice} \nComputer Win")
            self.computer_score_label.config(text=f"Computer Score: {self.computer_score}")
        if self.score == 3 or self.computer_score == 3:
            self.finish_game()

    def finish_game(self):
        messagebox.showinfo("Finish Game",
                            f"The Game is Finished \nYour Score: {self.score} \nComputer Score: {self.computer_score}")
        self.score = 0
        self.computer_score = 0
        self.your_score_label.config(text=f"Score: {self.score}")
        self.computer_score_label.config(text=f"Computer Score: {self.computer_score}")

    def reset_function(self):
        if self.score == 0 and self.computer_score == 0:
            messagebox.showinfo("Warning", "You can Start to Play")
        else:
            msg = messagebox.askquestion("Warning", "Are you sure you want to Reset the Game")
            if msg == "yes":
                self.score = 0
                self.computer_score = 0
                self.your_score_label.config(text=f"Score: {self.score}")
                self.computer_score_label.config(text=f"Computer Score: {self.computer_score}")

    def quit_function(self):
        msg = messagebox.askquestion("Warning", "Are you sure to Quit the Game", icon="warning")
        if msg == "yes":
            self.window.quit()

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = RPSGame()
    app.run()
