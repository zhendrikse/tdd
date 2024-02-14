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
PROXIMITY_TOLERANCE = 3


class Pacman(Movable):
    def __init__(self, initial_node: Node):
        self._start_node = initial_node
        self._target_node = None
        self._position = initial_node.coordinates
        self._direction = Direction.NONE

    @property
    def position(self):
        return self._position

    def _pacman_near_target(self) -> bool:
        return self._position.manhattan_distance_to(self._target_node.coordinates) < PROXIMITY_TOLERANCE

    def _pacman_near_start(self) -> bool:
        return self._position.manhattan_distance_to(self._start_node.coordinates) < PROXIMITY_TOLERANCE

    def move(self, direction: Direction, dt: float) -> None:
        if self._pacman_near_start():
            if self._start_node.has_neighbor_in(direction):
                self._target_node = self._start_node.neighbor_at(direction)
                self._calculate_new_position(direction, dt)
        elif self._pacman_near_target():
            self._set_new_target(direction, dt)
        elif direction.value == self._direction.value:
            self._calculate_new_position(direction, dt)
        elif direction.is_opposite_direction_of(self._direction):
            self._switch_start_and_target()
            self._calculate_new_position(direction, dt)
        else:
            # User tries to make pacman leave the vertices between the nodes
            pass

    def _set_new_target(self, direction: Direction, dt):
        if self._target_node.is_portal():
            self._start_node = self._target_node.portal_neighbor()
            self._position = self._start_node.coordinates
            self._calculate_new_position(direction, dt)
        if self._target_node.has_neighbor_in(direction):
            self._start_node = self._target_node
            self._target_node = self._start_node.neighbor_at(direction)
            self._calculate_new_position(direction, dt)

    def _switch_start_and_target(self):
        node = self._target_node
        self._target_node = self._start_node
        self._start_node = node

    def _calculate_new_position(self, direction: Direction, dt: float) -> None:
        increment = INCREMENTS[direction.value]
        self._position = Coordinates(self._position.x + increment.x * dt, self._position.y + increment.y * dt)
        self._recalibrate_pacman_on_vertex(direction)
        self._direction = direction

    def _recalibrate_pacman_on_vertex(self, direction: Direction):
        if direction.value == Direction.UP.value or direction.value == Direction.DOWN.value:
            self._position = Coordinates(self._start_node.coordinates.x, self._position.y)
        else:
            self._position = Coordinates(self._position.x, self._start_node.coordinates.y)

    def render(self, screen: Screen):
        screen.render_circle(YELLOW, self._position, RADIUS)
