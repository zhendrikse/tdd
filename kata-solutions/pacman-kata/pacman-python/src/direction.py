from enum import Enum


class Direction(Enum):
    NONE = "None"
    UP = "Up"
    DOWN = "Down"
    LEFT = "Left"
    RIGHT = "Right"

    @staticmethod
    def opposite_direction_of(direction):
        if direction == Direction.UP:
            return Direction.DOWN
        elif direction == Direction.DOWN:
            return Direction.UP
        elif direction == Direction.RIGHT:
            return Direction.LEFT
        elif direction == Direction.LEFT:
            return Direction.RIGHT
        else:
            return Direction.NONE
