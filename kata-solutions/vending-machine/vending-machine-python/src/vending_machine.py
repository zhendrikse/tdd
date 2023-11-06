from enum import Enum
from dataclasses import dataclass


class Can(Enum):
    NOTHING = "Nothing"
    COLA = "Cola"
    FANTA = "Fanta"


class Choice(Enum):
    COKE = "Coke"
    FIZZY_ORANGE = "Fizzy orange"
    BEER = "Beer"


class Cashier:
    def __init__(self):
        self._balance_in_cents = 0

    def insert(self, balance_in_cents: int) -> None:
        self._balance_in_cents += balance_in_cents

    def does_balance_allow(self, price_in_cents: int) -> bool:
        return self._balance_in_cents >= price_in_cents

    def buy(self, amount_in_cents: int) -> None:
        self._balance_in_cents -= amount_in_cents


@dataclass(frozen=True)
class Drawer:
    can: Can
    price_in_cents: int

    def deliver(self, cashier: Cashier) -> Can:
        if not cashier.does_balance_allow(self.price_in_cents):
            return Can.NOTHING

        cashier.buy(self.price_in_cents)
        return self.can


class VendingMachine:
    def __init__(self) -> None:
        self._choice_drawer_map: dict[Choice, Drawer] = {}
        self._cashier = Cashier()

    def insert(self, amount_in_cents) -> None:
        self._cashier.insert(amount_in_cents)

    def configure(self, choice: Choice, can: Can, price_in_cents: int = 0) -> None:
        self._choice_drawer_map[choice] = Drawer(can, price_in_cents)

    def deliver(self, choice: Choice) -> Can:
        if not choice in self._choice_drawer_map:
            return Can.NOTHING

        drawer = self._choice_drawer_map[choice]
        return drawer.deliver(self._cashier)
