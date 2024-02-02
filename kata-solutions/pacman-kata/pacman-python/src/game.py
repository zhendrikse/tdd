from circle import Circle
from game_event import GameEvent
from coordinates import Coordinates
from pygame_screen import PyGameScreen
from pygame_eventbus import PyGameEventBus
from pygame_clock import PyGameClock
from eventbus import EventBus
from clock import Clock
from screen import Screen


class Game:

    def __init__(self, eventbus: EventBus, clock: Clock, screen: Screen) -> None:
        self._sprite = Circle()
        self._eventbus = eventbus
        self._clock = clock
        self._screen = screen

    def run(self) -> None:
        keep_running = True
        dt = 0

        while keep_running:
            for event in self._eventbus.get_events():
                if event == GameEvent.QUIT:
                    keep_running = False

            self._tick(dt)
            dt = self._clock.tick(60)

        self._screen.quit()

    def _tick(self, dt) -> None:
        self._sprite.tick(dt)
        self._sprite.draw(self._screen)
        self._screen.flip()
        self._screen.fill("purple")

if __name__ == "__main__":
    game = Game(PyGameEventBus(), PyGameClock(), PyGameScreen(Coordinates(1280, 720)))
    game.run()
