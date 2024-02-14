from dataclasses import dataclass

from ..coordinates import Coordinates
from ..ports.screen import Screen, TILEWIDTH
from ..sprites.sprite import Sprite, WHITE

PELLET_RADIUS = 4
POWER_PELLET_RADIUS = 8


@dataclass(frozen=True)
class Pellet(Sprite):
    position: Coordinates
    is_power_pellet: bool = False

    def render(self, screen: Screen) -> None:
        radius = int(POWER_PELLET_RADIUS * TILEWIDTH / 16) \
            if self.is_power_pellet else int(PELLET_RADIUS * TILEWIDTH / 16)
        screen.render_circle(WHITE, self.position, radius)



