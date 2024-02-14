from dataclasses import dataclass
from enum import Enum

from ..coordinates import Coordinates
from ..ports.screen import Screen, TILEWIDTH
from ..sprites.sprite import Sprite, WHITE

PELLET_RADIUS = 4
POWER_PELLET_RADIUS = 8


class PelletPoints(Enum):
    ZERO = 0
    PELLET = 5
    POWER_PELLET = 10


@dataclass(frozen=True)
class Pellet(Sprite):
    position: Coordinates
    is_power_pellet: bool = False

    @property
    def radius(self):
        return int(POWER_PELLET_RADIUS * TILEWIDTH / 16) \
            if self.is_power_pellet else int(PELLET_RADIUS * TILEWIDTH / 16)

    @property
    def points(self) -> PelletPoints:
        return PelletPoints.POWER_PELLET if self.is_power_pellet else PelletPoints.PELLET

    def render(self, screen: Screen) -> None:
        screen.render_circle(WHITE, self.position, self.radius)



