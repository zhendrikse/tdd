from .command import Command
from .coordinates import Coordinates
from .ports.screen import TILEWIDTH
from .direction import Direction
from .node import Node
from .ports.screen import Screen
from .sprite import Sprite

YELLOW = (255, 255, 0)
PACMAN = 0
SPEED = 100 * TILEWIDTH / 16
INCREMENTS = {
    Direction.NONE.value: Coordinates(0, 0),
    Direction.UP.value: Coordinates(0, -1 * SPEED),
    Direction.DOWN.value: Coordinates(0, 1 * SPEED),
    Direction.LEFT.value: Coordinates(-1 * SPEED, 0),
    Direction.RIGHT.value: Coordinates(1 * SPEED, 0)}
RADIUS = 10
COLOR = YELLOW
PROXIMITY_TOLERANCE = 3


class Pacman(Sprite):
    def __init__(self, initial_node: Node):
        self._name = PACMAN
        self._start_node = initial_node
        self._target_node = None
        self._position = initial_node.coordinates
        self._direction = Direction.NONE

    def _pacman_near_target(self) -> bool:
        return self._position.manhattan_distance_to(self._target_node.coordinates) < PROXIMITY_TOLERANCE

    def _pacman_near_start(self) -> bool:
        return self._position.manhattan_distance_to(self._start_node.coordinates) < PROXIMITY_TOLERANCE

    def move(self, command: Command, dt: float) -> None:
        if self._pacman_near_start():
            if self._start_node.has_neighbor_in(command.direction):
                self._target_node = self._start_node.neighbor_at(command.direction)
                self._calculate_new_position(command, dt)
        elif self._pacman_near_target():
            self._set_new_target(command, dt)
        elif command.direction.value == self._direction.value:
            self._calculate_new_position(command, dt)
        elif command.direction.is_opposite_direction_of(self._direction):
            self._switch_start_and_target()
            self._calculate_new_position(command, dt)
        else:
            # User tries to make pacman leave the vertices between the nodes
            pass

    def _set_new_target(self, command, dt):
        if self._target_node.is_portal():
            self._start_node = self._target_node.portal_neighbor()
            self._position = self._start_node.coordinates
            self._calculate_new_position(command, dt)
        if self._target_node.has_neighbor_in(command.direction):
            self._start_node = self._target_node
            self._target_node = self._start_node.neighbor_at(command.direction)
            self._calculate_new_position(command, dt)

    def _switch_start_and_target(self):
        node = self._target_node
        self._target_node = self._start_node
        self._start_node = node

    def _calculate_new_position(self, command: Command, dt: float) -> None:
        increment = INCREMENTS[command.direction.value]
        self._position = Coordinates(self._position.x + increment.x * dt, self._position.y + increment.y * dt)
        self._recalibrate_pacman_on_vertex(command)
        self._direction = command.direction

    def _recalibrate_pacman_on_vertex(self, command):
        if command.direction.value == Direction.UP.value or command.direction.value == Direction.DOWN.value:
            self._position = Coordinates(self._start_node.coordinates.x, self._position.y)
        else:
            self._position = Coordinates(self._position.x, self._start_node.coordinates.y)

    def render(self, screen: Screen):
        screen.render_circle(COLOR, self._position, RADIUS)
