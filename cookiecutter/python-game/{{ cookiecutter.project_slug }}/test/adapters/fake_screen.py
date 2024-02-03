from typing import Protocol

from coordinates import Coordinates
from ports.screen import Screen
from test.observer import Observer


class FakeScreen(Screen):
    def __init__(self, observer: Observer):
        self._observer = observer

    def render_circle(self, color: str, coordinates: Coordinates, radius: int) -> None:
        self._observer.notify(f"Circle with radius {radius} rendered at {coordinates}")

    def refresh(self) -> None:
        self._observer.notify("refresh")

    def quit(self) -> None:
        self._observer.notify("quit")
