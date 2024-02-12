from dataclasses import dataclass

from .coordinates import Coordinates


@dataclass(frozen=True)
class Pellet:
    _position: Coordinates

