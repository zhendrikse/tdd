from dataclasses import dataclass

from .sprite import WHITE
from ..coordinates import Coordinates
from ..position_on_vertex import PositionOnVertex
from ..sprites.movable import Movable
from ..direction import Direction
from ..ports.screen import Screen

GHOST_RADIUS = 10


@dataclass(frozen=True)
class Ghost(Movable):
    position: PositionOnVertex

    @property
    def coordinates(self) -> Coordinates:
        return self.position.position

    def move(self, direction: Direction, dt: float) -> None:
        # only change direction when close to target
        new_direction = direction if self.position.is_close_to_end else self.position.direction

        # but do not back track
        if new_direction.is_opposite_direction_of(self.position.direction):
            return

        self.position.move(new_direction, dt)

    def render(self, screen: Screen):
        screen.render_circle(WHITE, self.coordinates, GHOST_RADIUS)