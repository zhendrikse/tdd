from abc import abstractmethod
from typing import Protocol
from .ports.screen import Screen
from .game_event import Command


class Sprite(Protocol):
    @abstractmethod
    def render(self, screen: Screen) -> None:
        ...

    @abstractmethod
    def update(self, direction: Command, dt: float) -> None:
        ...
