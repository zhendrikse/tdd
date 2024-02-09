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
        self._target_node = None
        self._position = initial_node.coordinates
        self._direction = Direction.NONE

    def _pacman_near_target(self) -> bool:
        return self._position.manhattan_distance_to(self._target_node.coordinates) < 5

    def _pacman_near_start(self) -> bool:
        return self._position.manhattan_distance_to(self._start_node.coordinates) < 5

    def update(self, command: Command, dt: float) -> None:
        if self._pacman_near_start():
            if self._start_node.direction_is_valid(command.direction):
                self._target_node = self._start_node.neighbor_at(command.direction)
                self._calculate_new_position(command, dt)
        elif self._pacman_near_target():
            if self._target_node.direction_is_valid(command.direction):
                self._start_node = self._target_node
                self._target_node = self._start_node.neighbor_at(command.direction)
                self._calculate_new_position(command, dt)
        elif command.direction.value == self._direction.value:
            self._calculate_new_position(command, dt)
        elif command.direction.is_opposite_direction_of(self._direction):
            self._switch_start_and_target()
            self._calculate_new_position(command, dt)
        else:
            # User tries to make pacman leave the vertices between the nodes
            pass

    def _switch_start_and_target(self):
        node = self._target_node
        self._target_node = self._start_node
        self._start_node = node

    def _calculate_new_position(self, command: Command, dt: float) -> None:
        increment = DIRECTIONS[command.direction.value]
        self._position = Coordinates(self._position.x + increment.x * dt, self._position.y + increment.y * dt)

        # Recalibrate pacman on vertex
        if command.direction.value == Direction.UP.value or command.direction.value == Direction.DOWN.value:
            self._position = Coordinates(self._start_node.coordinates.x, self._position.y)
        else:
            self._position = Coordinates(self._position.x, self._start_node.coordinates.y)

        self._direction = command.direction

    def render(self, screen: Screen):
        screen.render_circle(COLOR, self._position, RADIUS)
