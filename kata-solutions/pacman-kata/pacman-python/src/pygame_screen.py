import pygame
from coordinates import Coordinates


class PyGameScreen:
    def __init__(self, resolution):
        self._renderer = pygame.draw
        self._screen = pygame.display.set_mode((resolution.x, resolution.y))
        self._display = pygame.display
        pygame.init()

    def render_circle(self, color: str, coordinates: Coordinates, radius: int) -> None:
        self._renderer.circle(self._screen, color, (coordinates.x, coordinates.y), radius)

    def flip(self) -> None:
        self._display.flip()

    def fill(self, color) -> None:
        self._screen.fill(color)

    def quit(self) -> None:
        pygame.quit()

