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
DIRECTIONS = {
    Direction.NONE.value: Coordinates(0, 0),
    Direction.UP.value: Coordinates(0, -1 * SPEED),
    Direction.DOWN.value: Coordinates(0, 1 * SPEED),
    Direction.LEFT.value: Coordinates(-1 * SPEED, 0),
    Direction.RIGHT.value: Coordinates(1 * SPEED, 0)}
RADIUS = 10
COLOR = YELLOW


class Pacman(Sprite):
    def __init__(self, initial_node: Node):
        self._name = PACMAN
        self._start_node = initial_node
        self._target_node = initial_node
        self._position = initial_node.coordinates
        self._direction = Direction.NONE

    def _is_on_start_node(self) -> bool:
        return self._position.manhattan_distance_to(self._start_node.coordinates) < 3

    def _is_beyond_target_node(self, position: Coordinates) -> bool:
        distance_start_target = self._start_node.coordinates.manhattan_distance_to(self._target_node.coordinates)
        distance_pacman_from_start = self._start_node.coordinates.manhattan_distance_to(position)
        return distance_pacman_from_start > distance_start_target

    def update(self, command: Command, dt):
        if self._is_on_start_node():
            self._depart_from_start_node(command)

        new_position = self._calculate_new_position(command, dt)

        if self._is_beyond_target_node(new_position):
            self._target_node_reached()
        else:
            self._update_position(command, new_position)

    def _update_position(self, command, new_position):
        if command.direction == self._direction:
            self._position = new_position
        if command.direction == Direction.opposite_direction_of(self._direction):
            self._switch_start_and_target()
            self._position = new_position

    def _switch_start_and_target(self):
        node = self._target_node
        self._target_node = self._start_node
        self._start_node = node

    def _target_node_reached(self):
        self._direction = Direction.NONE
        self._start_node = self._target_node
        self._position = self._target_node.coordinates

    def _calculate_new_position(self, command, dt):
        increment = DIRECTIONS[command.direction.value]
        return Coordinates(self._position.x + increment.x * dt, self._position.y + increment.y * dt)

    def _depart_from_start_node(self, command):
        if self._start_node.direction_is_valid(command.direction):
            self._direction = command.direction
            self._target_node = self._start_node.neighbor_at(command.direction)

    def render(self, screen: Screen):
        screen.render_circle(COLOR, self._position, RADIUS)
