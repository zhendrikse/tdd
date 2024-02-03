from typing import Protocol, Tuple

from ..coordinates import Coordinates


class Screen(Protocol):

    def render_circle(self, color: Tuple[int, int, int], coordinates: Coordinates, radius: int) -> None:
        ...

    def refresh(self) -> None:
        ...

    def quit(self) -> None:
        ...

