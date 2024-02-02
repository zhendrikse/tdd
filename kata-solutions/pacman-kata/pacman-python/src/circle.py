from coordinates import Coordinates


class Circle:
    def __init__(self):
        self._xy = Coordinates(50, 50)

    def draw(self, game_engine):
        game_engine.draw_circle("red", self._xy, 40)

    def tick(self, dt):
        if self._xy.x <= 500:
            self._xy = Coordinates(self._xy.x + dt * 0.3, self._xy.y)
        else:
            self._xy = Coordinates(50, 50)
