from enum import Enum
from typing import Protocol, List


class GameEngine(Protocol):

    def draw_circle(self, color, coordinates, radius) -> None:
        ...

    def refresh(self) -> None:
        ...

    def tick(self, rate: int) -> int:
        ...

    def quit(self) -> None:
        ...

    def events(self) -> List[Enum]:
        ...
