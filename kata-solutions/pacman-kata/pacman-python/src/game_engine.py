import pygame
from enum import Enum
from game_event import GameEvent
from typing import List
from screen import Screen
from coordinates import Coordinates

class GameEngine:
    def __init__(self, screen):
        self._screen = screen
        self._clock = pygame.time.Clock()
        self._eventbus = pygame.event
        pygame.init()

    def tick(self, rate) -> int:
        return self._clock.tick(rate)

    def quit(self):
        pygame.quit()

    def draw_circle(self, color: str, coordinates: Coordinates, radius: int) -> None:
        self._screen.render_circle(color, coordinates, radius)

    def refresh(self) -> None:
        self._screen.flip()
        self._screen.fill("purple")

    def get_events(self) -> List[Enum]:
        for event in self._eventbus.get():
            if event.type == pygame.QUIT:
                return [GameEvent.QUIT]

        return []
