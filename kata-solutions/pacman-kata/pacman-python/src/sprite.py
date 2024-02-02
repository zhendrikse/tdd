from typing import Protocol


class Sprite(Protocol):
    def draw(self, gui):
        ...
