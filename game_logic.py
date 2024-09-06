# game_logic.py

class CheckersLogic:
    def __init__(self, board, scoreboard):
        self.board = board
        self.scoreboard = scoreboard
        self.current_turn = "red"  # "red" or "blue"
        self.selected_piece = None  # Track the selected piece
        self.valid_moves = []  # Track valid moves for selected piece

    def select_piece(self, row, col):
        """Handle piece selection and show valid moves."""
        piece_color = self.get_piece_color(row, col)
        if piece_color and piece_color == self.current_turn:
            self.selected_piece = (row, col)
            self.valid_moves = self.get_valid_moves(row, col)
            self.highlight_moves()
        else:
            self.selected_piece = None
            self.clear_highlights()

    def move_piece(self, row, col):
        """Move the selected piece if the move is valid."""
        if (row, col) in self.valid_moves:
            start_row, start_col = self.selected_piece

            # Clear original tile
            self.board.tiles[start_row][start_col].delete("all")

            # Move the piece to the new tile
            self.board.place_piece(row, col, self.current_turn)

            # Check for captures and remove opponent's piece if captured
            if abs(row - start_row) == 2:  # Capture move
                capture_row = (row + start_row) // 2
                capture_col = (col + start_col) // 2
                self.board.tiles[capture_row][capture_col].delete("all")
                self.scoreboard.update_score(self.current_turn)

            # Switch the turn after a successful move
            self.switch_turn()
        self.selected_piece = None
        self.clear_highlights()

    def get_valid_moves(self, row, col):
        """Return valid moves for the selected piece."""
        piece_color = self.get_piece_color(row, col)
        direction = -1 if piece_color == "red" else 1  # Red moves up, Blue moves down
        valid_moves = []

        # Check the diagonal moves (left and right)
        for d_col in [-1, 1]:
            new_row = row + direction
            new_col = col + d_col
            if self.is_on_board(new_row, new_col) and not self.get_piece_color(new_row, new_col):
                valid_moves.append((new_row, new_col))  # Normal move

            # Check for capture moves
            capture_row = row + 2 * direction
            capture_col = col + 2 * d_col
            if self.is_on_board(capture_row, capture_col) and not self.get_piece_color(capture_row, capture_col):
                opponent_color = "blue" if piece_color == "red" else "red"
                if self.get_piece_color(new_row, new_col) == opponent_color:
                    valid_moves.append((capture_row, capture_col))  # Capture move

        return valid_moves

    def get_piece_color(self, row, col):
        """Return the color of the piece at the given position."""
        items = self.board.tiles[row][col].find_all()
        if items:
            color = self.board.tiles[row][col].itemcget(items[0], "fill")
            return color
        return None

    def highlight_moves(self):
        """Highlight the valid moves for the selected piece."""
        for row, col in self.valid_moves:
            self.board.tiles[row][col].config(bg="#90EE90")  # Light green for valid moves

    def clear_highlights(self):
        """Clear the highlighted moves."""
        for row in range(self.board.size):
            for col in range(self.board.size):
                color = "white" if (row + col) % 2 == 0 else "black"
                self.board.tiles[row][col].config(bg=color)

    def switch_turn(self):
        """Switch turns between players."""
        self.current_turn = "blue" if self.current_turn == "red" else "red"

    def is_on_board(self, row, col):
        """Check if a position is on the board."""
        return 0 <= row < self.board.size and 0 <= col < self.board.size
