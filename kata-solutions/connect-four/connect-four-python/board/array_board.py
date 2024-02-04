from board.board import Board, Disc

COLUMNS = 7
ROWS = 6
RED_4 = [Disc.RED.value for i in range(4)]
YELLOW_4 = [Disc.YELLOW.value for i in range(4)]


class ArrayBoard(Board):
    def __init__(self) -> None:
        self.board = [[0] * COLUMNS for i in range(ROWS)]
        self.moves = ""

    def get_row_count(self):
        return ROWS

    def get_col_count(self):
        return COLUMNS

    def amount_discs_in_col(self, col: int) -> int:
        filled_rows = [row for row in range(ROWS) if self.board[row][col] == Disc.NONE.value]
        return ROWS - len(filled_rows)

    def is_valid_move(self, move: int):
        return move > 0 and move <= COLUMNS and self.amount_discs_in_col(move - 1) < ROWS

    def undo_last_move(self):
        last_col = int(self.moves[-1]) - 1
        self.moves = self.moves[:-1]
        self.board[self.amount_discs_in_col(last_col) - 1][last_col] = Disc.NONE.value

    def insert_disc_at(self, move: int, disc: Disc) -> None:
        if not self.is_valid_move(move):
            raise ValueError("Illegal move")

        col = move - 1
        self.moves += str(move)
        self.board[self.amount_discs_in_col(col)][col] = disc.value

    @staticmethod
    def from_string(moves: str):
        board = ArrayBoard()
        player = Disc.RED
        for move in moves:
            board.insert_disc_at(int(move), player)
            player = Disc.YELLOW if player == Disc.RED else Disc.RED

        return board

    def has_four(self, sequence):
        for index in range(len(sequence) - 3):
            if sequence[index:index + 4] == RED_4 or sequence[index:index + 4] == YELLOW_4:
                return True
        return False

    def has_horizontal_four(self):
        return len([row for row in range(ROWS) if self.has_four([self.board[row][col] for col in range(COLUMNS)])]) != 0

    def has_vertical_four(self):
        return len(
            [col for col in range(COLUMNS) if self.has_four([self.board[row][col] for row in range(ROWS)])]) != 0

    def has_diagonal_four(self):
        for i in range(ROWS):
            if self.has_four(self.top_down_diagonal(i, 3)) or \
                    self.has_four(self.bottom_up_diagonal(i, 3)):
                return True

    def has_connect_four(self):
        return self.has_horizontal_four() or \
            self.has_vertical_four() or \
            self.has_diagonal_four()

    def move_cursor_top_left(self, row: int, col: int):
        row_cursor, col_cursor = row, col
        while min((ROWS - 1) - row_cursor, col_cursor) != 0:
            row_cursor += 1
            col_cursor -= 1
        return row_cursor, col_cursor

    def move_cursor_bottom_left(self, row: int, col: int):
        row_cursor, col_cursor = row, col
        while min(row_cursor, col_cursor) != 0:
            row_cursor -= 1
            col_cursor -= 1
        return row_cursor, col_cursor

    def diagonal(self, row: int, col: int, delta_x: int, delta_y: int):
        diagonal = []
        row_cursor, col_cursor = row, col
        while row_cursor >= 0 and row_cursor < ROWS and col_cursor < COLUMNS:
            diagonal.append(self.board[row_cursor][col_cursor])
            row_cursor += delta_y
            col_cursor += delta_x
        return diagonal

    def top_down_diagonal(self, row: int, col: int) -> str:
        row_cursor, col_cursor = self.move_cursor_top_left(row, col)
        return self.diagonal(row_cursor, col_cursor, 1, -1)

    def bottom_up_diagonal(self, row: int, col: int) -> str:
        row_cursor, col_cursor = self.move_cursor_bottom_left(row, col)
        return self.diagonal(row_cursor, col_cursor, 1, 1)

    def __str__(self):
        board_repr = "|"
        for row in reversed(range(ROWS)):
            for col in range(COLUMNS):
                board_repr += str(Disc(self.board[row][col])) + "|"
            if row != 0:
                board_repr += "\n|"
        board_repr += "\n  1  2  3  4  5  6  7 "
        return board_repr
