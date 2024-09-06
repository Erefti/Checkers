# game_board.py

import tkinter as tk

class GameBoard:
    def __init__(self, master, on_piece_selected, on_piece_moved):
        self.master = master
        self.on_piece_selected = on_piece_selected
        self.on_piece_moved = on_piece_moved
        self.size = 8  # 8x8 board
        self.tiles = []
        self.selected_piece = None
        self.create_board()

    def create_board(self):
        # Create a grid of tiles (8x8 checkered pattern)
        for row in range(self.size):
            tile_row = []
            for col in range(self.size):
                color = "white" if (row + col) % 2 == 0 else "black"
                tile = tk.Canvas(self.master, width=60, height=60, bg=color, highlightthickness=0)
                tile.grid(row=row, column=col)
                tile.bind("<Button-1>", lambda event, r=row, c=col: self.on_tile_clicked(r, c))
                tile_row.append(tile)
            self.tiles.append(tile_row)

        # Add Checkers pieces (for simplicity, this starts with a basic configuration)
        self.initialize_pieces()

    def initialize_pieces(self):
        # Add pieces for player 1 (top rows)
        for row in range(3):
            for col in range(self.size):
                if (row + col) % 2 != 0:
                    self.place_piece(row, col, "red")

        # Add pieces for player 2 (bottom rows)
        for row in range(5, self.size):
            for col in range(self.size):
                if (row + col) % 2 != 0:
                    self.place_piece(row, col, "blue")

    def place_piece(self, row, col, color):
        piece = self.tiles[row][col].create_oval(10, 10, 50, 50, fill=color, outline="black")
        self.tiles[row][col].tag_bind(piece, "<Button-1>", lambda event, r=row, c=col: self.on_piece_selected(r, c))

    def on_tile_clicked(self, row, col):
        if self.selected_piece:
            # If a piece is already selected, attempt to move
            self.on_piece_moved(self.selected_piece[0], self.selected_piece[1], row, col)
            self.selected_piece = None
        else:
            # Select the piece
            self.selected_piece = (row, col)
            self.on_piece_selected(row, col)

    def reset_board(self):
        # Clear board for restarting the game
        for row in range(self.size):
            for col in range(self.size):
                self.tiles[row][col].delete("all")
        self.initialize_pieces()
