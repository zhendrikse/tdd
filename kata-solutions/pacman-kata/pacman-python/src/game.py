from circle import Circle
from pygame_game_engine import PyGameGameEngine
from game_event import GameEvent
from coordinates import Coordinates


class Game:

    def __init__(self, game_engine=PyGameGameEngine(Coordinates(1280, 720))):
        self._sprite = Circle()
        self._game_engine = game_engine

    def run(self):
        running = True
        dt = 0

        while running:
            for event in self._game_engine.events():
                if event == GameEvent.QUIT:
                    running = False

            self._tick(dt)
            dt = self._game_engine.tick(60)

        self._game_engine.quit()

    def _tick(self, dt) -> None:
        self._sprite.tick(dt)
        self._sprite.draw(self._game_engine)
        self._game_engine.refresh()


if __name__ == "__main__":
    Game().run()
