from circle import Circle
from game_event import KeyPress, GameEvent
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
        dx_dy = Coordinates(0, 0)

        while keep_running:
            # print(f"Rendering with dx-xy={dx_dy}")
            self._render(dx_dy)
            for event in self._eventbus.get_events():
                # print(f"Received event {event}")
                if event.is_quit():
                    keep_running = False
                elif event.is_arrow_key():
                    dx_dy = Coordinates(event.key_press_value[0], event.key_press_value[1])

        self._screen.quit()

    def _render(self, dx_dy: Coordinates) -> None:
        self._sprite.update_coordinates(dx_dy)
        self._sprite.draw(self._screen)
        self._screen.refresh()


if __name__ == "__main__":
    game = Game(PyGameEventBus(), PyGameClock(), PyGameScreen())
    game.run()
