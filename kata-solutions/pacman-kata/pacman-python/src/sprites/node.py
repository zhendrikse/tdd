from dataclasses import dataclass, field
from enum import Enum
from typing import Any, List

from ..coordinates import Coordinates
from ..direction import Direction
from ..ports.screen import Screen
from ..sprites.sprite import Sprite, RED, WHITE


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

NEIGHBOR_TO_DIRECTION_MAP = {
    NeighborType.LEFT: Direction.LEFT,
    NeighborType.RIGHT: Direction.RIGHT,
    NeighborType.UP: Direction.UP,
    NeighborType.DOWN: Direction.DOWN
}


@dataclass(frozen=True)
class Node(Sprite):
    position: Coordinates
    neighbors: dict[NeighborType | Any] = field(default_factory=dict)

    @property
    def coordinates(self):
        return self.position

    def is_portal(self) -> bool:
        return NeighborType.PORTAL in self.neighbors.keys()

    def portal_neighbor(self):
        return self.neighbors[NeighborType.PORTAL]

    def render(self, screen: Screen) -> None:
        screen.render_circle(RED, self.position, 12)
        _ = [screen.render_line(WHITE, self.position, node.coordinates, 4)
             for node in self.neighbors.values()]

    def set_neighbor(self, new_neighbor: Any, neighbor_type: NeighborType) -> None:
        self.neighbors[neighbor_type] = new_neighbor

    def neighbor_at(self, direction: Direction) -> Any:
        neighbor_type = DIRECTION_TO_NEIGHBOR_MAP[direction]
        return self.neighbors[neighbor_type]

    def valid_directions(self) -> List[Direction]:
        return [NEIGHBOR_TO_DIRECTION_MAP[neighbor_type]
                for neighbor_type in self.neighbors.keys() if neighbor_type != NeighborType.PORTAL]
