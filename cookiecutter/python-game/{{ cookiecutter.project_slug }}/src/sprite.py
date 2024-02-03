from typing import Protocol
from .ports.screen import Screen
from .coordinates import Coordinates


class Sprite(Protocol):
    def draw(self, screen: Screen) -> None:
        ...

    def update_coordinates(self, increment: Coordinates) -> None:
        ...
