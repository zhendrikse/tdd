from abc import abstractmethod
from typing import Protocol
from ..ports.screen import Screen


WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)


class Sprite(Protocol):
    @abstractmethod
    def render(self, screen: Screen) -> None:
        ...
