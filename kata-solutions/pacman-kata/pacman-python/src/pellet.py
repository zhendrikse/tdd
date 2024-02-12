from dataclasses import dataclass

from .coordinates import Coordinates


@dataclass(frozen=True)
class Pellet:
    position: Coordinates
    is_power_pellet: bool = False


