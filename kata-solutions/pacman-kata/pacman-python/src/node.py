from enum import Enum
from typing import Any

from .coordinates import Coordinates
from .ports.screen import Screen

WHITE = (255, 255, 255)
RED = (255, 0, 0)


class Orientation(Enum):
    UP = "UP"
    DOWN = "DOWN"
    LEFT = "LEFT"
    RIGHT = "RIGHT"


class Node:
    def __init__(self, position: Coordinates) -> None:
        self._position: Coordinates = position
        self._neighbors: [Orientation | Node] = {}

    @property
    def coordinates(self):
        return self._position

    def render(self, screen: Screen) -> None:
        screen.render_circle(RED, self._position, 12)
        _ = [screen.render_line(WHITE, self._position, node.coordinates, 4)
             for node in self._neighbors.values()]

    def set_neighbor(self, new_neighbor: Any, orientation: Orientation):
        self._neighbors[orientation] = new_neighbor
