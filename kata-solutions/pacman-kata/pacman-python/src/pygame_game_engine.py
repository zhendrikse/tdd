import pygame
from enum import Enum
from game_event import GameEvent
from typing import List


class PyGameGameEngine:
    def __init__(self, resolution):
        self._renderer = pygame
        self._screen = pygame.display.set_mode((resolution.x, resolution.y))
        self._clock = pygame.time.Clock()
        pygame.init()

    def draw_circle(self, color, coordinates, radius) -> None:
        self._renderer.draw.circle(self._screen, color, (coordinates.x, coordinates.y), radius)

    def refresh(self) -> None:
        self._renderer.display.flip()
        self._screen.fill("purple")

    def tick(self, rate: int) -> int:
        return self._clock.tick(rate)

    def quit(self):
        self._renderer.quit()

    def _map_events(self) -> List[Enum]:
        for event in self._renderer.event.get():
            if event.type == pygame.QUIT:
                return [GameEvent.QUIT]

        return []

    def events(self) -> List[Enum]:
        return self._map_events()
