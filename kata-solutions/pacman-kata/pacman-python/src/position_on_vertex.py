from typing import List

from .coordinates import Coordinates
from .ports.screen import TILEWIDTH
from .direction import Direction
from .sprites.node import Node
from .vertex import Vertex

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


class PositionOnVertex:
    def __init__(self, initial_node: Node):
        self._vertex = Vertex(initial_node, initial_node)
        self._position = initial_node.coordinates

    @property
    def position(self) -> Coordinates:
        return self._position

    def valid_directions(self) -> List[Direction]:
        if self._position.is_close_to(self._vertex.start.coordinates):
            return self._vertex.start.valid_directions()
        elif self._position.is_close_to(self._vertex.end.coordinates):
            return self._vertex.end.valid_directions()
        else:
            return [self._vertex.direction]

    def move(self, direction: Direction, dt: float) -> None:
        if direction.is_opposite_direction_of(self._vertex.direction):
            self._vertex = self._vertex.switch_start_and_end()
            self._calculate_new_position(direction, dt)
            return

        if self._position.is_close_to(self._vertex.end.coordinates) and self._vertex.end.is_portal():
            self._vertex = Vertex(self._vertex.end.portal_neighbor(), self._vertex.end)
            self._position = self._vertex.start.coordinates
            self._calculate_new_position(direction, dt)
            return

        if direction in self.valid_directions():
            if self._position.is_close_to(self._vertex.start.coordinates):
                self._vertex = self._vertex.vertex_from_start_in_direction(direction)
            elif self._position.is_close_to(self._vertex.end.coordinates):
                self._vertex = self._vertex.vertex_from_end_in_direction(direction)
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
