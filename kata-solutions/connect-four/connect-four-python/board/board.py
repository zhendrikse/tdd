from enum import Enum
from abc import ABC, abstractmethod

class Disc(Enum):
  NONE = 0
  RED = 1
  YELLOW = 2

  def __str__(self):
    disc_repr = '🔴' if self.value == Disc.RED.value else '  '
    return '🟡' if self.value == Disc.YELLOW.value else disc_repr

class Board(ABC):

  @abstractmethod
  def get_row_count(self):
    pass

  @abstractmethod
  def get_col_count(self):
    pass

  @abstractmethod
  def is_valid_move(self, move: int):
    pass

  @abstractmethod
  def undo_last_move(self):
    pass
    
  """
  Insert a disc at a given column. The first column is one.
  """
  @abstractmethod 
  def insert_disc_at(self, move: int, disc:Disc) -> None:
    pass

  """
  Initialize a board from string.
  4433562 then leads to
    0 0 0 0 0 0 0
    0 0 0 0 0 0 0
    0 0 0 0 0 0 0
    0 0 0 0 0 0 0
    0 0 2 2 0 0 0
    0 1 1 1 1 2 0
  """
  @staticmethod
  def from_string(moves: str):
    pass

  @abstractmethod
  def has_connect_four(self):
    pass
