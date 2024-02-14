from dataclasses import dataclass

PROXIMITY_TOLERANCE = 3


class Coordinates:
    pass


@dataclass(frozen=True)
class Coordinates:
    x: int = 0
    y: int = 0

    def distance_squared_to(self, other: Coordinates) -> int:
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2

    def is_close_to(self, other: Coordinates) -> bool:
        return self.distance_squared_to(other) < PROXIMITY_TOLERANCE ** 2

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"<{int(self.x)}, {int(self.y)}>"
