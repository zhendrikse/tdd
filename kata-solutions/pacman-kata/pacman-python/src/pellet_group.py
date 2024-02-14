from dataclasses import dataclass
from typing import List

from .coordinates import Coordinates
from .sprites.pacman import COLLISION_RADIUS
from .sprites.pellet import Pellet, PelletPoints


@dataclass(frozen=True)
class PelletGroup:
    pellets: List[Pellet]

    def render(self, screen):
        _ = [pellet.render(screen) for pellet in self.pellets]

    def remove_pellet_when_pacman_is_close(self, pacman_position: Coordinates) -> PelletPoints:
        eatable_pellets = [pellet for pellet in self.pellets if self._is_close(pellet, pacman_position)]
        if len(eatable_pellets) != 0:
            self.pellets.remove(eatable_pellets[0])
            return PelletPoints.POWER_PELLET if eatable_pellets[0].is_power_pellet else PelletPoints.PELLET
        else:
            return PelletPoints.ZERO

    # Circle A has a radius of RA.
    # Circle B has a radius of RB.
    #
    # Distance D is the actual distance between the two circles.
    # If the distance D is greater than the sum of the circle's radii,
    # then the circles can't be colliding.  RA + RB < D.
    #
    # If the distance D is less than or equal to the sum of the circle's radii,
    # then the circles are colliding.  RA + RB >= D.
    # See https://pacmancode.com/eating-pellets
    @staticmethod
    def _is_close(pellet: Pellet, pacman_position: Coordinates) -> bool:
        distance_squared = (pellet.position.x - pacman_position.x) ** 2 + (pellet.position.y - pacman_position.y) ** 2
        radii_squared = (pellet.radius + COLLISION_RADIUS) ** 2
        return distance_squared <= radii_squared
