from dataclasses import dataclass


@dataclass(frozen=True)
class Coordinates:
    x: int = 0
    y: int = 0

    def manhattan_distance_to(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"<{int(self.x)}, {int(self.y)}>"
