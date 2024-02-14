from dataclasses import dataclass

from .direction import Direction
from .sprites.node import Node


class Vertex:
    pass


@dataclass(frozen=True)
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
