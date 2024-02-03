from coordinates import Coordinates
from ports.screen import Screen
from sprite import Sprite


class Circle(Sprite):
    def __init__(self):
        self._xy = Coordinates(50, 50)

    def draw(self, screen: Screen) -> None:
        screen.render_circle("red", self._xy, 10)

    def tick(self, dt: int) -> None:
        if self._xy.x <= 400:
            self._xy = Coordinates(self._xy.x + dt * 0.3, self._xy.y)
        else:
            self._xy = Coordinates(50, 50)
