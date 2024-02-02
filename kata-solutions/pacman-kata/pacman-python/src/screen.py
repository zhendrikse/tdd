import pygame
from coordinates import Coordinates

class Screen:
    def __init__(self, resolution):
        self._renderer = pygame.draw
        self._screen = pygame.display.set_mode((resolution.x, resolution.y))
        self._display = pygame.display

    def render_circle(self, color: str, coordinates: Coordinates, radius: int) -> None:
        self._renderer.circle(self._screen, color, (coordinates.x, coordinates.y), radius)

    def flip(self):
        self._display.flip()

    def fill(self, color):
        self._screen.fill(color)
