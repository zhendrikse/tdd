import pygame
from coordinates import Coordinates
from ports.screen import Screen

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
        self._renderer = pygame.draw
        self._screen = pygame.display.set_mode(SCREENSIZE, pygame.SHOWN, BITS_USED_FOR_COLOR)
        self._display = pygame.display
        self._background = pygame.surface.Surface(SCREENSIZE).convert()
        self._background.fill(BLACK)
        pygame.init()

    def render_circle(self, color: str, coordinates: Coordinates, radius: int) -> None:
        self._renderer.circle(self._screen, color, (coordinates.x, coordinates.y), radius)

    def refresh(self) -> None:
        self._display.update()
        self._screen.fill(BLACK)

    def quit(self) -> None:
        pygame.quit()
