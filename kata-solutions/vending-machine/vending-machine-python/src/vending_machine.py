from enum import Enum

class Can(Enum):
  NOTHING = "Nothing"
  COLA = "Cola"
  FANTA = "Fanta"

class Choice(Enum):
  COKE = "Coke"
  FIZZY_ORANGE = "Fizzy orange"
  BEER = "Beer"
  
class VendingMachine:
  def __init__(self) -> None:
    self._choice_can_map: dict[Choice, Can] = {}

  def configure(self, choice: Choice, can: Can) -> None:
    self._choice_can_map[choice] = can
    
  def deliver(self, choice: Choice) -> Can:
    if not choice in self._choice_can_map:
      return Can.NOTHING
    return self._choice_can_map[choice]
    
