from enum import Enum

class Can(Enum):
  NOTHING = "Nothing"
  COLA = "Cola"

class Choice(Enum):
  COKE = "Coke"
  
class VendingMachine:
  def __init__(self):
    self._can_of_choice = Can.NOTHING

  def configure(self, choice: Choice, can: Can) -> None:
    self._can_of_choice = can
    
  def deliver(self, choice: Choice) -> Can:
    return self._can_of_choice
    
