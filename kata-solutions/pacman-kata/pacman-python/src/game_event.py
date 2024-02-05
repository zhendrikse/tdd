from enum import Enum

from src.command import Command
from src.direction import Direction


class KeyPress(Enum):
    ARROW_UP_PRESSED = [0, -1]
    ARROW_UP_RELEASED = [0, 0]
    ARROW_DOWN_PRESSED = [0, 1]
    ARROW_DOWN_RELEASED = [0, 0]
    ARROW_LEFT_PRESSED = [-1, 0]
    ARROW_LEFT_RELEASED = [0, 0]
    ARROW_RIGHT_PRESSED = [1, -0]
    ARROW_RIGHT_RELEASED = [0, 0]


class GameEvent:
    def __init__(self, keypress: KeyPress = None, do_quit=False):
        self._key_event = keypress
        self._quit = do_quit

    def is_quit(self) -> bool:
        return self._quit

    def is_not_a_keyboard_event(self) -> bool:
        return self._key_event is None

    def as_command(self) -> Command:
        if self._key_event.value == KeyPress.ARROW_UP_PRESSED.value:
            return Command(Direction.UP)
        if self._key_event.value == KeyPress.ARROW_DOWN_PRESSED.value:
            return Command(Direction.DOWN)
        if self._key_event.value == KeyPress.ARROW_LEFT_PRESSED.value:
            return Command(Direction.LEFT)
        if self._key_event.value == KeyPress.ARROW_RIGHT_PRESSED.value:
            return Command(Direction.RIGHT)
        
        return Command(Direction.NONE)

    def is_arrow_key(self) -> bool:
        if self.is_not_a_keyboard_event():
            return False

        return self._key_event.value in [
            KeyPress.ARROW_UP_PRESSED.value,
            KeyPress.ARROW_RIGHT_PRESSED.value,
            KeyPress.ARROW_LEFT_PRESSED.value,
            KeyPress.ARROW_DOWN_PRESSED.value,
            KeyPress.ARROW_UP_RELEASED.value,
            KeyPress.ARROW_RIGHT_RELEASED.value,
            KeyPress.ARROW_LEFT_RELEASED.value,
            KeyPress.ARROW_DOWN_RELEASED.value]

    def __str__(self):
        return f"GameEvent = [{self._key_event}, quit={self._quit}]"
