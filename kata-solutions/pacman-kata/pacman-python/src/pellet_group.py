from dataclasses import dataclass
from typing import List

from .pellet import Pellet


@dataclass(frozen=True)
class PelletGroup:
    pellets: List[Pellet]
