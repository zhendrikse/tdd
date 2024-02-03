from .coordinates import Coordinates
from .ports.screen import Screen
from .sprite import Sprite


class Circle(Sprite):
    def __init__(self):
        self._xy = Coordinates(50, 50)

    def draw(self, screen: Screen) -> None:
        screen.render_circle("red", self._xy, 10)

    def update_coordinates(self, increment: Coordinates) -> None:
        self._xy = Coordinates(self._xy.x + increment.x, self._xy.y + increment.y)
