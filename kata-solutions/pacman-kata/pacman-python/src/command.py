from dataclasses import dataclass

from .direction import Direction


@dataclass(frozen=True)
class Command:
    direction: Direction
