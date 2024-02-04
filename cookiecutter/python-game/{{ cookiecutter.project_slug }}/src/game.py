from enum import Enum

from .adapters.pygame_screen import PyGameScreen
from .adapters.pygame_eventbus import PyGameEventBus
from .adapters.pygame_clock import PyGameClock
from .ports.eventbus import EventBus
from .ports.clock import Clock
from .ports.screen import Screen
from .pacman import Pacman
from .game_event import Command


class Game:

    def __init__(self, eventbus: EventBus, clock: Clock, screen: Screen) -> None:
        self._pacman = Pacman()
        self._eventbus = eventbus
        self._clock = clock
        self._screen = screen

    def run(self) -> None:
        keep_running = True
        direction = Command.STOP

        while keep_running:
            dt = self._clock.tick(30) / 1000.0
            self._render(direction, dt)
            for event in self._eventbus.get_events():
                #  print(f"Received event {event}, direction is now {direction}")
                if event.is_arrow_key():
                    direction = event.as_command()
                if event.is_quit():
                    keep_running = False

        self._screen.quit()

    def _render(self, direction: Command, dt: float) -> None:
        # print(f"Rendering with direction={direction} and dt={dt}")
        self._pacman.update(direction, dt)
        self._pacman.render(self._screen)
        self._screen.refresh()


if __name__ == "__main__":
    game = Game(PyGameEventBus(), PyGameClock(), PyGameScreen())
    game.run()
