from dataclasses import dataclass
from typing import List

from .coordinates import Coordinates
from .direction import Direction
from .node import Node
from .ports.screen import Screen, TILEWIDTH, TILEHEIGHT

NODE_SYMBOL = "+"
SPACE_SYMBOL = "X"
LINE_SYMBOL = "."


@dataclass(frozen=True)
class NodeGroup:
    _nodes: List[Node]

    def is_empty(self) -> bool:
        return len(self._nodes) == 0

    def first(self) -> Node:
        return self._nodes[0]

    def render(self, screen: Screen) -> None:
        _ = [node.render(screen) for node in self._nodes]

    @classmethod
    def from_string(cls, text_based_node_group: str):
        game_as_string = text_based_node_group.replace(" ", "")

        if not NODE_SYMBOL in text_based_node_group:
            return NodeGroup([])

        list_of_lines = game_as_string.splitlines()
        dimension = Coordinates(len(list_of_lines[0]), len(list_of_lines))

        list_of_nodes = [cls._parse_line(i, list_of_lines[i]) for i in range(dimension.y)]

        # transposed_lines_list =
        # transposed_nodes_list =

        flattened_list = [node for node_list in list_of_nodes for node in node_list]
        return NodeGroup(flattened_list)

    @classmethod
    def _parse_line(cls, line_number, line: str):
        node_positions = [position for position, char in enumerate(line) if char == NODE_SYMBOL]
        nodes = cls._determine_nodes(node_positions, TILEHEIGHT * line_number)
        cls._determine_horizontal_vertices(node_positions, nodes, line)
        return nodes

    @classmethod
    def _determine_horizontal_vertices(cls, node_positions, nodes, line):
        for node_counter in range(len(node_positions) - 1):
            if line[node_positions[node_counter] + 1] == LINE_SYMBOL:
                nodes[node_counter].set_neighbor(nodes[node_counter + 1], Direction.RIGHT)
                nodes[node_counter + 1].set_neighbor(nodes[node_counter], Direction.LEFT)

    @classmethod
    def _determine_nodes(cls, node_positions: List[int], y: int):
        nodes = []
        _ = [nodes.append(Node(Coordinates(TILEWIDTH * position, y))) for position in node_positions]
        return nodes
