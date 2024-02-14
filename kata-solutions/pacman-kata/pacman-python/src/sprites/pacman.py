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


class Vertex:
    pass


@dataclass
class Vertex:
    start: Node
    end: Node

    def vertex_from_start_in_direction(self, direction: Direction) -> Vertex:
        return Vertex(self.start, self.start.neighbor_at(direction))

    def vertex_from_end_in_direction(self, direction: Direction) -> Vertex:
        return Vertex(self.end, self.end.neighbor_at(direction))

    def switch_start_and_end(self) -> Vertex:
        return Vertex(self.end, self.start)

    @property
    def direction(self):
        distance_x = self.end.coordinates.x - self.start.coordinates.x
        distance_y = self.end.coordinates.y - self.start.coordinates.y
        if distance_x == 0:
            return Direction.DOWN if distance_y > 0 else Direction.UP
        else:
            return Direction.RIGHT if distance_x > 0 else Direction.LEFT


class Pacman(Movable):
    def __init__(self, initial_node: Node):
        self._vertex = Vertex(initial_node, initial_node)
        self._position = initial_node.coordinates

    @property
    def position(self):
        return self._position

    def move(self, direction: Direction, dt: float) -> None:
        if self._position.is_close_to(self._vertex.start.coordinates) and self._vertex.start.has_neighbor_in(direction):
            self._vertex = self._vertex.vertex_from_start_in_direction(direction)
        elif self._position.is_close_to(self._vertex.end.coordinates):
            if self._vertex.end.is_portal():
                self._vertex = Vertex(self._vertex.end.portal_neighbor(), self._vertex.end)
                self._position = self._vertex.start.coordinates
            elif self._vertex.end.has_neighbor_in(direction):
                self._vertex = self._vertex.vertex_from_end_in_direction(direction)
            else:
                return  # pacman cannot move into this direction
        elif direction.is_opposite_direction_of(self._vertex.direction):
            self._vertex = self._vertex.switch_start_and_end()
        elif direction != self._vertex.direction:
            return  # pacman cannot depart from its vertex

        self._calculate_new_position(direction, dt)

    def _calculate_new_position(self, direction: Direction, dt: float) -> None:
        increment = INCREMENTS[direction.value]
        self._position = Coordinates(self._position.x + increment.x * dt, self._position.y + increment.y * dt)
        self._recalibrate_pacman_on_vertex()

    def _recalibrate_pacman_on_vertex(self):
        if self._vertex.direction == Direction.UP or self._vertex.direction == Direction.DOWN:
            self._position = Coordinates(self._vertex.start.coordinates.x, self._position.y)
        else:
            self._position = Coordinates(self._position.x, self._vertex.end.coordinates.y)

    def render(self, screen: Screen):
        screen.render_circle(YELLOW, self._position, RADIUS)
