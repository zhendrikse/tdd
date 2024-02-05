from typing import Tuple

import pygame
from ..coordinates import Coordinates
from ..ports.screen import Screen, SCREENSIZE

BLACK = (0, 0, 0)
BITS_USED_FOR_COLOR = 32


class PyGameScreen(Screen):
    def __init__(self):
        self._pygame = pygame
        self._screen = pygame.display.set_mode(SCREENSIZE, pygame.SHOWN, BITS_USED_FOR_COLOR)
        self._background = None
        self.set_background()
        self._pygame.init()

    def set_background(self) -> None:
        self._background = pygame.surface.Surface(SCREENSIZE).convert()
        self._background.fill(BLACK)

    def blit(self) -> None:
        self._screen.blit(self._background, (0, 0))

    def render_circle(self, color: Tuple[int, int, int], coordinates: Coordinates, radius: int) -> None:
        self._pygame.draw.circle(self._screen, color, (coordinates.x, coordinates.y), radius)

    def update(self) -> None:
        self._pygame.display.update()

    def quit(self) -> None:
        self._pygame.quit()

    def render_line(self, color: Tuple[int, int, int], line_start: Coordinates, line_end: Coordinates, width: int):
        self._pygame.draw.line(self._screen, color, (line_start.x, line_start.y), (line_end.x, line_end.y), width)

