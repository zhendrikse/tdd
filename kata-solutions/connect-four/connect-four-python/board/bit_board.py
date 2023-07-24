from board.board import Board, Disc

COLUMNS = 7
ROWS = 6

class BitBoard(Board):
  def __init__(self) -> None:
    self.board_red
    self.board_yellow

  def get_row_count(self):
    return ROWS

  def get_col_count(self):
    return COLUMNS
