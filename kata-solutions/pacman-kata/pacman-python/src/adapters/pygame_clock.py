import pygame
from ..ports.clock import Clock


class PyGameClock(Clock):
    def __init__(self):
        self._clock = pygame.time.Clock()

    def tick(self, rate: float) -> int:
        return self._clock.tick()
