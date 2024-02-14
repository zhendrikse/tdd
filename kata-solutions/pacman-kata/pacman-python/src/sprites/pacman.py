from dataclasses import dataclass

from .sprite import YELLOW
from ..coordinates import Coordinates
from ..sprites.movable import Movable
from ..ports.screen import TILEWIDTH
from ..direction import Direction
from ..sprites.node import Node
from ..ports.screen import Screen

COLLISION_RADIUS = 5
PACMAN_RADIUS = 10
SPEED = 100 * TILEWIDTH / 16
INCREMENTS = {
    Direction.NONE.value: Coordinates(0, 0),
    Direction.UP.value: Coordinates(0, -1 * SPEED),
    Direction.DOWN.value: Coordinates(0, 1 * SPEED),
    Direction.LEFT.value: Coordinates(-1 * SPEED, 0),
    Direction.RIGHT.value: Coordinates(1 * SPEED, 0)}
RADIUS = 10


class Path:
    pass


@dataclass
class Path:
    start: Node
    end: Node

    def path_from_start_in_direction(self, direction: Direction) -> Path:
        return Path(self.start, self.start.neighbor_at(direction))

    def path_from_end_in_direction(self, direction: Direction) -> Path:
        return Path(self.end, self.end.neighbor_at(direction))

    def switch_start_and_end(self) -> Path:
        return Path(self.end, self.start)

    @property
    def direction(self):
        distance_x = self.end.coordinates.x - self.start.coordinates.x
        distance_y = self.end.coordinates.y - self.start.coordinates.y
        if distance_x == 0:
            if distance_y > 0:
                return Direction.DOWN
            if distance_y < 0:
                return Direction.UP
        elif distance_y == 0:
            if distance_x > 0:
                return Direction.RIGHT
            if distance_y < 0:
                return Direction.LEFT
        return Direction.NONE


class Pacman(Movable):
    def __init__(self, initial_node: Node):
        self._path = Path(initial_node, initial_node)
        self._position = initial_node.coordinates
        self._direction = Direction.NONE

    @property
    def position(self):
        return self._position

    def move(self, direction: Direction, dt: float) -> None:
        if self._position.is_close_to(self._path.start.coordinates) and self._path.start.has_neighbor_in(direction):
            self._path = Path(self._path.start, self._path.start.neighbor_at(direction))
        elif self._position.is_close_to(self._path.end.coordinates):
            if self._path.end.is_portal():
                self._path = Path(self._path.end.portal_neighbor(), self._path.end)
                self._position = self._path.start.coordinates
            elif self._path.end.has_neighbor_in(direction):
                self._path = Path(self._path.end, self._path.end.neighbor_at(direction))
            else:
                return  # pacman cannot move into this direction
        elif direction.is_opposite_direction_of(self._path.direction):
            self._path = self._path.switch_start_and_end()
        elif direction != self._direction:
            return  # pacman cannot depart from its vertex

        self._calculate_new_position(direction, dt)

    def _calculate_new_position(self, direction: Direction, dt: float) -> None:
        increment = INCREMENTS[direction.value]
        self._position = Coordinates(self._position.x + increment.x * dt, self._position.y + increment.y * dt)
        self._recalibrate_pacman_on_vertex(direction)
        self._direction = direction

    def _recalibrate_pacman_on_vertex(self, direction: Direction):
        if self._path.direction == Direction.UP or self._path.direction == Direction.DOWN:
            self._position = Coordinates(self._path.start.coordinates.x, self._position.y)
        else:
            self._position = Coordinates(self._position.x, self._path.end.coordinates.y)

    def render(self, screen: Screen):
        screen.render_circle(YELLOW, self._position, RADIUS)
