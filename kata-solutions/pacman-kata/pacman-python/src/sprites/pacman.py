from dataclasses import dataclass

from .sprite import YELLOW
from ..coordinates import Coordinates
from ..position_on_vertex import PositionOnVertex
from ..sprites.movable import Movable
from ..direction import Direction
from ..sprites.node import Node
from ..ports.screen import Screen

COLLISION_RADIUS = 5
PACMAN_RADIUS = 10
RADIUS = 10


@dataclass(frozen=True)
class Pacman(Movable):
    position: PositionOnVertex

    @property
    def coordinates(self) -> Coordinates:
        return self.position.position

    def move(self, direction: Direction, dt: float) -> None:
        self.position.move(direction, dt)

    def render(self, screen: Screen):
        screen.render_circle(YELLOW, self.coordinates, RADIUS)
