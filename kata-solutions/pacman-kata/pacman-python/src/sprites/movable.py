from abc import abstractmethod

from ..direction import Direction
from ..sprites.sprite import Sprite


class Movable(Sprite):

    @abstractmethod
    def move(self, direction: Direction, dt: float) -> None:
        ...
