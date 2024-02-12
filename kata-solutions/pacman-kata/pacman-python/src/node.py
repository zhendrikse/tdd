from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict

from .coordinates import Coordinates
from .direction import Direction
from .ports.screen import Screen

WHITE = (255, 255, 255)
RED = (255, 0, 0)


class NeighborType(Enum):
    PORTAL = "Portal"
    UP = "Up"
    DOWN = "Down"
    LEFT = "Left"
    RIGHT = "Right"


DIRECTION_TO_NEIGHBOR_MAP = {
    Direction.LEFT: NeighborType.LEFT,
    Direction.RIGHT: NeighborType.RIGHT,
    Direction.UP: NeighborType.UP,
    Direction.DOWN: NeighborType.DOWN
}


@dataclass(frozen=True)
class Node:
    position: Coordinates
    neighbors: dict[NeighborType | Any] = field(default_factory=dict)

    @property
    def coordinates(self):
        return self.position

    def has_neighbor_in(self, direction: Direction) -> bool:
        if direction in DIRECTION_TO_NEIGHBOR_MAP.keys():
            neighbor_type = DIRECTION_TO_NEIGHBOR_MAP[direction]
            return neighbor_type in self.neighbors.keys()
        else:
            return False

    def is_portal(self) -> bool:
        return NeighborType.PORTAL in self.neighbors.keys()

    def portal_neighbor(self):
        return self.neighbors[NeighborType.PORTAL]

    def render(self, screen: Screen) -> None:
        screen.render_circle(RED, self.position, 12)
        _ = [screen.render_line(WHITE, self.position, node.coordinates, 4)
             for node in self.neighbors.values()]

    def set_neighbor(self, new_neighbor: Any, type: NeighborType) -> None:
        self.neighbors[type] = new_neighbor

    def neighbor_at(self, direction: Direction) -> Any:
        neighbor_type = DIRECTION_TO_NEIGHBOR_MAP[direction]
        return self.neighbors[neighbor_type]
