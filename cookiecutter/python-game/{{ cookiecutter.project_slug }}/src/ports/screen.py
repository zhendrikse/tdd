from typing import Protocol

from ..coordinates import Coordinates


class Screen(Protocol):

    def render_circle(self, color: str, coordinates: Coordinates, radius: int) -> None:
        ...

    def refresh(self) -> None:
        ...

    def quit(self) -> None:
        ...

