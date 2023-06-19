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
    self._choice_price_map: dict[Choice, int] = {}
    self._balance_in_cents = 0

  def insert(self, amount_in_cents):
    self._balance_in_cents = amount_in_cents
  
  def configure(self, choice: Choice, can: Can, price_in_cents: int = 0) -> None:
    self._choice_can_map[choice] = can
    self._choice_price_map[choice] = price_in_cents
    
  def deliver(self, choice: Choice) -> Can:
    if not choice in self._choice_can_map:
      return Can.NOTHING

    price = self._choice_price_map[choice]
    if self._balance_in_cents >= price:
      self._balance_in_cents -= price
      return self._choice_can_map[choice] 
    
    return Can.NOTHING
    
