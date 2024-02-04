from typing import Tuple

from src.coordinates import Coordinates
from src.ports.screen import Screen
from ..observer import Observer


class FakeScreen(Screen):
    def __init__(self, observer: Observer):
        self._observer = observer

    def render_circle(self, color: Tuple[int, int, int], coordinates: Coordinates, radius: int) -> None:
        self._observer.notify(f"Circle with radius {radius} rendered at {coordinates}")

    def render_line(self, color: Tuple[int, int, int], line_start: Coordinates, line_end: Coordinates, width: int):
        self._observer.notify(f"Line between {line_start} and {line_end} with width={width}")

    def update(self) -> None:
        self._observer.notify("update")

    def blit(self) -> None:
        self._observer.notify("blit")

    def quit(self) -> None:
        self._observer.notify("quit")

    def set_background(self) -> None:
        self._observer.notify("Set background")

