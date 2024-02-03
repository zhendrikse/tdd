from .coordinates import Coordinates
from .adapters.pygame_screen import TILEWIDTH
from .ports.screen import Screen
from .sprite import Sprite
from .game_event import Command

YELLOW = (255, 255, 0)


PACMAN = 0
SPEED = 100 * TILEWIDTH / 16
DIRECTIONS = {
    Command.STOP: Coordinates(0, 0),
    Command.UP: Coordinates(0, -1 * SPEED),
    Command.DOWN: Coordinates(0, 1 * SPEED),
    Command.LEFT: Coordinates(-1 * SPEED, 0),
    Command.RIGHT: Coordinates(1 * SPEED, 0)}
RADIUS = 10
COLOR = YELLOW


class Pacman(Sprite):
    def __init__(self):
        self._name = PACMAN
        self._position = Coordinates(200, 400)
        self._direction = Command.STOP

    def update(self, direction: Command, dt):
        increment = DIRECTIONS[self._direction]
        self._position = Coordinates(self._position.x + increment.x * dt, self._position.y + increment.y * dt)
        self._direction = direction

    def render(self, screen: Screen):
        screen.render_circle(COLOR, self._position, RADIUS)
