from typing import Protocol

from coordinates import Coordinates


class FakeScreen:

    def render_circle(self, color: str, coordinates: Coordinates, radius: int) -> None:
        ...

    def flip(self) -> None:
        ...

    def fill(self, color) -> None:
        ...

    def quit(self) -> None:
        ...

