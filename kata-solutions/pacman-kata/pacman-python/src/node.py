from enum import Enum
from typing import Any, List

from .coordinates import Coordinates
from .direction import Direction
from .ports.screen import Screen

WHITE = (255, 255, 255)
RED = (255, 0, 0)


class Node:
    def __init__(self, position: Coordinates) -> None:
        self._position: Coordinates = position
        self._neighbors: [Direction | Node] = {}

    @property
    def coordinates(self):
        return self._position

    def direction_is_valid(self, direction: Direction) -> bool:
        return direction in [direction for direction in self._neighbors.keys()]

    def render(self, screen: Screen) -> None:
        screen.render_circle(RED, self._position, 12)
        _ = [screen.render_line(WHITE, self._position, node.coordinates, 4)
             for node in self._neighbors.values()]

    def set_neighbor(self, new_neighbor: Any, direction: Direction) -> None:
        self._neighbors[direction] = new_neighbor

    def neighbor_at(self, direction: Direction) -> Any:
        return self._neighbors[direction]
