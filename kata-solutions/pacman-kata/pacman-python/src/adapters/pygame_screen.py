from typing import Tuple

import pygame
from ..coordinates import Coordinates
from ..ports.screen import Screen

TILEWIDTH = 16
TILEHEIGHT = 16
NROWS = 36
NCOLS = 28
SCREENWIDTH = NCOLS * TILEWIDTH
SCREENHEIGHT = NROWS * TILEHEIGHT
SCREENSIZE = (SCREENWIDTH, SCREENHEIGHT)
BLACK = (0, 0, 0)
BITS_USED_FOR_COLOR = 32


class PyGameScreen(Screen):
    def __init__(self):
        self._pygame = pygame
        self._screen = pygame.display.set_mode(SCREENSIZE, pygame.SHOWN, BITS_USED_FOR_COLOR)
        self._background = None
        self._pygame.init()

    def set_background(self) -> None:
        self._background = pygame.surface.Surface(SCREENSIZE).convert()
        self._background.fill(BLACK)

    def render_circle(self, color: Tuple[int, int, int], coordinates: Coordinates, radius: int) -> None:
        self._pygame.draw.circle(self._screen, color, (coordinates.x, coordinates.y), radius)

    def refresh(self) -> None:
        self._pygame.display.update()
        self._screen.fill(BLACK)

    def quit(self) -> None:
        self._pygame.quit()

    def render_line(self, color: Tuple[int, int, int], line_start: Coordinates, line_end: Coordinates, width: int):
        self._pygame.draw.line(self._screen, color, (line_start.x, line_start.y), (line_end.x, line_end.y), width)

