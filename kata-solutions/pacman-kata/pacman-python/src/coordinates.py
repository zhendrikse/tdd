from dataclasses import dataclass


@dataclass(frozen=True)
class Coordinates:
    _x: int = 0
    _y: int = 0

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y