from enum import Enum


class KeyPress(Enum):
    ARROW_UP_PRESSED = [0, -1]
    ARROW_UP_RELEASED = [0, 0]
    ARROW_DOWN_PRESSED = [0, 1]
    ARROW_DOWN_RELEASED = [0, 0]
    ARROW_LEFT_PRESSED = [-1, 0]
    ARROW_LEFT_RELEASED = [0, 0]
    ARROW_RIGHT_PRESSED = [1, -0]
    ARROW_RIGHT_RELEASED = [0, 0]


class Command(Enum):
    STOP = 0
    UP = 1
    DOWN = -1
    LEFT = 2
    RIGHT = -2


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
            return Command.UP
        if self._key_event.value == KeyPress.ARROW_DOWN_PRESSED.value:
            return Command.DOWN
        if self._key_event.value == KeyPress.ARROW_LEFT_PRESSED.value:
            return Command.LEFT
        if self._key_event.value == KeyPress.ARROW_RIGHT_PRESSED.value:
            return Command.RIGHT
        
        return Command.STOP

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
