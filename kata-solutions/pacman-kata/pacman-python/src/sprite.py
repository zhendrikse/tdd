from abc import abstractmethod
from typing import Protocol
from .ports.screen import Screen
from .direction import Direction


class Sprite(Protocol):
    @abstractmethod
    def render(self, screen: Screen) -> None:
        ...

    @abstractmethod
    def move(self, direction: Direction, dt: float) -> None:
        ...
