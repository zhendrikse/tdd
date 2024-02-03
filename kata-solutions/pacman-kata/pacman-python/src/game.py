from circle import Circle
from game_event import GameEvent
from coordinates import Coordinates
from adapters.pygame_screen import PyGameScreen
from adapters.pygame_eventbus import PyGameEventBus
from adapters.pygame_clock import PyGameClock
from ports.eventbus import EventBus
from ports.clock import Clock
from ports.screen import Screen


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
                if event.value == GameEvent.QUIT.value:
                    keep_running = False

            self._tick(dt)
            dt = self._clock.tick(60)

        self._screen.quit()

    def _tick(self, dt) -> None:
        self._sprite.tick(dt)
        self._sprite.draw(self._screen)
        self._screen.refresh()


if __name__ == "__main__":
    game = Game(PyGameEventBus(), PyGameClock(), PyGameScreen(Coordinates(1280, 720), "purple"))
    game.run()
