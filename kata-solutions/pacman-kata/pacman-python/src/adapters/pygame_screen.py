import pygame
from coordinates import Coordinates
from ports.screen import Screen

TILEWIDTH = 32
TILEHEIGHT = 32
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
        self._background = pygame.surface.Surface(SCREENSIZE).convert()
        self._background.fill(BLACK)
        self._pygame.init()

    def render_circle(self, color: str, coordinates: Coordinates, radius: int) -> None:
        self._pygame.draw.circle(self._screen, color, (coordinates.x, coordinates.y), radius)

    def refresh(self) -> None:
        self._pygame.display.update()
        self._screen.fill(BLACK)

    def quit(self) -> None:
        self._pygame.quit()
