from dataclasses import dataclass
from typing import List

from .sprites.pellet import Pellet


@dataclass(frozen=True)
class PelletGroup:
    pellets: List[Pellet]

    def render(self, screen):
        _ = [pellet.render(screen) for pellet in self.pellets]
