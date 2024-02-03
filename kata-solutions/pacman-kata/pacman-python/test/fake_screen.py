from typing import Protocol

from coordinates import Coordinates
from test.observer import Observer


class FakeScreen:
    def __init__(self, observer: Observer):
        self._observer = observer

    def render_circle(self, color: str, coordinates: Coordinates, radius: int) -> None:
        self._observer.notify(f"Circle with radius {radius} rendered at {coordinates}")

    def flip(self) -> None:
        self._observer.notify("flip")

    def fill(self, color) -> None:
        self._observer.notify(f"fill with {color}")

    def quit(self) -> None:
        self._observer.notify("quit")
