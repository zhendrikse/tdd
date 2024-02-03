from typing import Protocol
from .ports.screen import Screen
from .game_event import Command


class Sprite(Protocol):
    def render(self, screen: Screen) -> None:
        ...

    def update(self, direction: Command, dt: float) -> None:
        ...
