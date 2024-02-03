from typing import Protocol
from ports.screen import Screen


class Sprite(Protocol):
    def draw(self, screen: Screen) -> None:
        ...

    def tick(self, dt: int) -> None:
        ...
