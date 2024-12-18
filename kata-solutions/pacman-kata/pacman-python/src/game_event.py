from enum import Enum

from .direction import Direction


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

    def as_command(self) -> Direction:
        if self._key_event is None:
            return Direction.NONE
        elif self._key_event.value == KeyPress.ARROW_UP_PRESSED.value:
            return Direction.UP
        elif self._key_event.value == KeyPress.ARROW_DOWN_PRESSED.value:
            return Direction.DOWN
        elif self._key_event.value == KeyPress.ARROW_LEFT_PRESSED.value:
            return Direction.LEFT
        elif self._key_event.value == KeyPress.ARROW_RIGHT_PRESSED.value:
            return Direction.RIGHT
        else:
            return Direction.NONE

    def __repr__(self):
        return f"GameEvent = [{self._key_event}, quit={self._quit}]"
