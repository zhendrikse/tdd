from dataclasses import dataclass


@dataclass(frozen=True)
class Coordinates:
    x: int = 0
    y: int = 0

    def __str__(self):
        return f"<{self.x}, {self.y}>"
