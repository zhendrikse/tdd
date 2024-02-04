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

