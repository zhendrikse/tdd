import pygame


class PyGameClock:
    def __init__(self):
        self._clock = pygame.time.Clock()

    def tick(self, rate: int) -> int:
        return self._clock.tick()
