from enum import Enum


class GameEvent(Enum):
    QUIT = 'quit'
    ARROW_UP_PRESSED = 'arrow up pressed'
    ARROW_UP_RELEASED = 'arrow up released'
    ARROW_DOWN_PRESSED = 'arrow down pressed'
    ARROW_DOWN_RELEASED = 'arrow down released'
    ARROW_LEFT_PRESSED = 'arrow left pressed'
    ARROW_LEFT_RELEASED = 'arrow left released'
    ARROW_RIGHT_PRESSED = 'arrow right pressed'
    ARROW_RIGHT_RELEASED = 'arrow right released'


