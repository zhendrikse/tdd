from enum import Enum


class Direction(Enum):
    NONE = "No direction"
    UP = "Up"
    DOWN = "Down"
    LEFT = "Left"
    RIGHT = "Right"

    def is_opposite_direction_of(self, direction) -> bool:
        return (direction.value == Direction.UP.value and self.value == Direction.DOWN.value or
                direction.value == Direction.DOWN.value and self.value == Direction.UP.value or
                direction.value == Direction.LEFT.value and self.value == Direction.RIGHT.value or
                direction.value == Direction.RIGHT.value and self.value == Direction.LEFT.value)

