from dataclasses import dataclass

from ..coordinates import Coordinates
from ..ports.screen import Screen, TILEWIDTH
from ..sprites.sprite import Sprite, WHITE


@dataclass(frozen=True)
class Pellet(Sprite):
    position: Coordinates
    is_power_pellet: bool = False

    def render(self, screen: Screen) -> None:
        screen.render_circle(WHITE, self.position, int(4 * TILEWIDTH / 16))



