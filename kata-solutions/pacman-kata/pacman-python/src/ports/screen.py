from abc import abstractmethod
from typing import Protocol, Tuple

from ..coordinates import Coordinates


class Screen(Protocol):
    @abstractmethod
    def render_circle(self, color: Tuple[int, int, int], coordinates: Coordinates, radius: int) -> None:
        ...

    @abstractmethod
    def refresh(self) -> None:
        ...

    @abstractmethod
    def quit(self) -> None:
        ...

    @abstractmethod
    def render_line(self, color: Tuple[int, int, int], line_start: Coordinates, line_end: Coordinates, width: int):
        ...

    @abstractmethod
    def set_background(self) -> None:
        ...
