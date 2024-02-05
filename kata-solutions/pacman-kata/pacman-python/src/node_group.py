from typing import List

from .node import Node
from .ports.screen import Screen


class NodeGroup(object):
    def __init__(self, node_group: List[Node]):
        self._nodes: List[Node] = node_group

    def is_empty(self) -> bool:
        return len(self._nodes) == 0

    def first(self) -> Node:
        return self._nodes.pop()

    def render(self, screen: Screen) -> None:
        _ = [node.render(screen) for node in self._nodes]
