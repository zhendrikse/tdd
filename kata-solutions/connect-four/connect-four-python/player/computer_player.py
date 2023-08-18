from abc import ABC, abstractmethod

class ComputerPlayer(ABC):
  @abstractmethod
  def calculate_next_move(self) -> int:
    pass