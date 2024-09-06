# scoreboard.py

import tkinter as tk

class Scoreboard:
    def __init__(self, master):
        self.master = master
        self.score = {"red": 0, "blue": 0}
        self.frame = tk.Frame(self.master, bg="#f0f0f0", padx=10, pady=10)
        self.frame.pack(side="right", fill="y")

        self.red_score_label = tk.Label(self.frame, text="Red: 0", font=("Arial", 14), bg="#f0f0f0")
        self.red_score_label.pack(pady=10)

        self.blue_score_label = tk.Label(self.frame, text="Blue: 0", font=("Arial", 14), bg="#f0f0f0")
        self.blue_score_label.pack(pady=10)

    def update_score(self, color):
        self.score[color] += 1
        self.red_score_label.config(text=f"Red: {self.score['red']}")
        self.blue_score_label.config(text=f"Blue: {self.score['blue']}")
