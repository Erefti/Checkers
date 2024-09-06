# welcome_page.py

import tkinter as tk

class WelcomePage:
    def __init__(self, master, start_callback):
        self.master = master
        self.master.title("Checkers Game")

        # Frame for Welcome Page
        self.frame = tk.Frame(self.master, bg="#4CAF50", padx=20, pady=20)
        self.frame.pack(fill="both", expand=True)

        # Welcome Label
        self.welcome_label = tk.Label(self.frame, text="Welcome to Checkers!", font=("Arial", 24, "bold"), bg="#4CAF50", fg="white")
        self.welcome_label.pack(pady=20)

        # Start Game Button
        self.start_button = tk.Button(self.frame, text="Start Game", font=("Arial", 18), command=start_callback, bg="white", fg="#4CAF50", padx=10, pady=5)
        self.start_button.pack(pady=20)
