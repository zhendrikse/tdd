from dataclasses import dataclass
from typing import List
from src.sprites.node import Node
from .ports.screen import Screen


@dataclass(frozen=True)
class NodeGroup:
    nodes: List[Node]
    render_group: bool = True

    def is_empty(self) -> bool:
        return len(self.nodes) == 0

    def first(self) -> Node:
        return self.nodes[0]

    def render(self, screen: Screen) -> None:
        if self.render_group:
            _ = [node.render(screen) for node in self.nodes]

