import pygame
from coordinates import Coordinates
from ports.screen import Screen


class PyGameScreen(Screen):
    def __init__(self, resolution, background_color: str):
        self._renderer = pygame.draw
        self._screen = pygame.display.set_mode((resolution.x, resolution.y))
        self._display = pygame.display
        self._background_color = background_color
        pygame.init()

    def render_circle(self, color: str, coordinates: Coordinates, radius: int) -> None:
        self._renderer.circle(self._screen, color, (coordinates.x, coordinates.y), radius)

    def refresh(self) -> None:
        self._display.update()
        self._screen.fill(self._background_color)

    def quit(self) -> None:
        pygame.quit()
