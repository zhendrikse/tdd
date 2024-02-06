from dataclasses import dataclass
from typing import List

from .coordinates import Coordinates
from .direction import Direction
from .node import Node
from .ports.screen import Screen, TILEWIDTH, TILEHEIGHT


@dataclass(frozen=True)
class NodeGroup:
    _nodes: List[Node]

    def is_empty(self) -> bool:
        return len(self._nodes) == 0

    def first(self) -> Node:
        return self._nodes[0]

    def render(self, screen: Screen) -> None:
        _ = [node.render(screen) for node in self._nodes]

