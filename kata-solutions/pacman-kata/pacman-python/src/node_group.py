from typing import List

from .coordinates import Coordinates
from .node import Orientation, Node
from .ports.screen import Screen


class NodeGroup(object):
    def __init__(self, node_group: List[Node]):
        self._nodes: List[Node] = node_group

    def render(self, screen: Screen) -> None:
        _ = [node.render(screen) for node in self._nodes]
