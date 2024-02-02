from circle import Circle
from game_engine import GameEngine
from game_event import GameEvent
from coordinates import Coordinates
from screen import Screen
from pygame_eventbus import PyGameEventBus
from pygame_clock import PyGameClock


class Game:

    def __init__(self, game_engine):
        self._sprite = Circle()
        self._game_engine = game_engine

    def run(self) -> None:
        keep_running = True
        dt = 0

        while keep_running:
            for event in self._game_engine.get_events():
                if event == GameEvent.QUIT:
                    keep_running = False

            self._tick(dt)
            dt = self._game_engine.tick(60)

        self._game_engine.quit()

    def _tick(self, dt) -> None:
        self._sprite.tick(dt)
        self._sprite.draw(self._game_engine)
        self._game_engine.refresh()


if __name__ == "__main__":
    screen = Screen(Coordinates(1280, 720))
    clock = PyGameClock()
    event_bus = PyGameEventBus()
    game = Game(GameEngine(screen, clock, event_bus))
    game.run()
