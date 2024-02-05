from typing import List

from .coordinates import Coordinates
from .direction import Direction
from .node import Node
from .ports.screen import Screen, TILEWIDTH, TILEHEIGHT

NODE_SYMBOL = "+"
SPACE_SYMBOL = "X"
LINE_SYMBOL = "."


class NodeGroup(object):
    def __init__(self, node_group: List[Node]):
        self._nodes: List[Node] = node_group

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

        game_nodes = cls._nodes_with_horizontal_vertices(game_as_string.splitlines())

        return NodeGroup(game_nodes)

    @classmethod
    def _nodes_with_horizontal_vertices(cls, lines):
        list_of_node_lists = [cls._parse_line(i, lines[i]) for i in range(len(lines))]
        # Return the flattened list
        return [item for node_list in list_of_node_lists for item in node_list]

    @classmethod
    def _parse_line(cls, line_number, line: str):
        node_positions = [position for position, char in enumerate(line) if char == NODE_SYMBOL]
        nodes = cls._determine_nodes(node_positions, TILEHEIGHT * line_number)
        cls._determine_horizontal_vertices(node_positions, nodes, line)
        return nodes

    @classmethod
    def _determine_horizontal_vertices(cls, node_positions, nodes, text_based_node_group):
        for node_counter in range(len(node_positions) - 1):
            if text_based_node_group[node_positions[node_counter] + 1] == LINE_SYMBOL:
                nodes[node_counter].set_neighbor(nodes[node_counter + 1], Direction.RIGHT)
                nodes[node_counter + 1].set_neighbor(nodes[node_counter], Direction.LEFT)

    @classmethod
    def _determine_nodes(cls, node_positions: List[int], y: int):
        nodes = []
        _ = [nodes.append(Node(Coordinates(TILEWIDTH * position, y))) for position in node_positions]
        return nodes

