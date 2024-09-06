# main.py

import tkinter as tk
from welcome_page import WelcomePage
from game_board import GameBoard
from game_logic import CheckersLogic
from scoreboard import Scoreboard

class CheckersApp:
    def __init__(self, root):
        self.root = root
        self.welcome_page = WelcomePage(self.root, self.start_game)

    def start_game(self):
        # Clear welcome page
        for widget in self.root.winfo_children():
            widget.destroy()

        # Setup game components
        self.board_frame = tk.Frame(self.root)
        self.board_frame.pack(side="left")
        
        self.board = GameBoard(self.board_frame, self.on_piece_selected, self.on_piece_moved)
        self.scoreboard = Scoreboard(self.root)
        self.logic = CheckersLogic(self.board, self.scoreboard)

    def on_piece_selected(self, row, col):
        # Handle piece selection in game logic
        self.logic.select_piece(row, col)

    def on_piece_moved(self, start_row, start_col, end_row, end_col):
        # Handle piece movement in game logic
        self.logic.move_piece(end_row, end_col)

if __name__ == "__main__":
    root = tk.Tk()
    app = CheckersApp(root)
    root.mainloop()
