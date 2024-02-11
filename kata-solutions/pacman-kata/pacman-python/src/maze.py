from dataclasses import dataclass, field
from typing import List

from .coordinates import Coordinates
from .node import Node, NeighborType
from .node_group import NodeGroup
from .ports.screen import TILEHEIGHT, TILEWIDTH

NODE_WITH_PELLET_SYMBOL = "+"
NODE_WITH_POWER_PELLET_SYMBOL = "P"
NODE_WITHOUT_PELLET_SYMBOL = "N"
SPACE_SYMBOL = "X"
PELLET_SYMBOL = "."
POWER_PELLET_SYMBOL = "p"
H_CONNECTION_WITHOUT_PELLET_SYMBOL = "-"
V_CONNECTION_WITHOUT_PELLET_SYMBOL = "|"

PACMAN_MAZE = '''X X X X X X X X X X X X X X X X X X X X X X X X X X X X
X X X X X X X X X X X X X X X X X X X X X X X X X X X X
X X X X X X X X X X X X X X X X X X X X X X X X X X X X
X X X X X X X X X X X X X X X X X X X X X X X X X X X X
X + . . . . + . . . . . + X X + . . . . . + . . . . + X
X . X X X X . X X X X X . X X . X X X X X . X X X X . X
X . X X X X . X X X X X . X X . X X X X X . X X X X . X
X . X X X X . X X X X X . X X . X X X X X . X X X X . X
X + . . . . + . . + . . + . . + . . + . . + . . . . + X
X . X X X X . X X . X X X X X X X X . X X . X X X X . X
X . X X X X . X X . X X X X X X X X . X X . X X X X . X
X + . . . . + X X + . . + X X + . . + X X + . . . . + X
X X X X X X . X X X X X . X X . X X X X X . X X X X X X
X X X X X X . X X X X X . X X . X X X X X . X X X X X X
X X X X X X . X X + . . + . . + . . + X X . X X X X X X
X X X X X X . X X . X X X = = X X X . X X . X X X X X X
X X X X X X . X X . X X X X X X X X . X X . X X X X X X
+ . . . . . + . . + X X X X X X X X + . . + . . . . . +
X X X X X X . X X . X X X X X X X X . X X . X X X X X X
X X X X X X . X X . X X X X X X X X . X X . X X X X X X
X X X X X X . X X + . . . . . . . . + X X . X X X X X X
X X X X X X . X X . X X X X X X X X . X X . X X X X X X
X X X X X X . X X . X X X X X X X X . X X . X X X X X X
X + . . . . + . . + . . + X X + . . + . . + . . . . + X
X . X X X X . X X X X X . X X . X X X X X . X X X X . X
X . X X X X . X X X X X . X X . X X X X X . X X X X . X
X + . + X X + . . + . . + . . + . . + . . + X X + . + X
X X X . X X . X X . X X X X X X X X . X X . X X . X X X
X X X . X X . X X . X X X X X X X X . X X . X X . X X X
X + . + . . + X X + . . + X X + . . + X X + . . + . + X
X . X X X X X X X X X X . X X . X X X X X X X X X X . X
X . X X X X X X X X X X . X X . X X X X X X X X X X . X
X + . . . . . . . . . . + . . + . . . . . . . . . . + X
X X X X X X X X X X X X X X X X X X X X X X X X X X X X
X X X X X X X X X X X X X X X X X X X X X X X X X X X X
X X X X X X X X X X X X X X X X X X X X X X X X X X X X
'''


@dataclass(frozen=True)
class Maze:
    _maze_as_string: str
    _nodes: List[Node] = field(default_factory=list)

    @property
    def _maze_lines(self) -> List[str]:
        maze_as_string = self._maze_as_string.replace(" ", "")
        return maze_as_string.splitlines()

    @property
    def _transposed_maze_lines(self) -> List[str]:
        transposed_lines_list = ["" for _ in range(len(self._maze_lines[0]))]
        for i in range(len(self._maze_lines[0])):
            for j in range(len(self._maze_lines)):
                transposed_lines_list[i] += self._maze_lines[j][i]
        return transposed_lines_list

    def as_node_group(self) -> NodeGroup:
        if NODE_WITH_PELLET_SYMBOL not in self._maze_as_string:
            return NodeGroup([])

        node_coordinates = self._determine_node_coordinates()
        flattened_node_coordinates = [coordinate for node_list in node_coordinates for coordinate in node_list]

        for coordinate in flattened_node_coordinates:
            self._create_node_with_neighbors(coordinate)

        return NodeGroup(self._nodes)

    def _determine_node_coordinates(self) -> List[List[Coordinates]]:
        node_coordinates = []
        for y in range(len(self._maze_lines)):
            line = self._maze_lines[y]
            x_coordinates_of_notes = [x for x, char in enumerate(line) if char == NODE_WITH_PELLET_SYMBOL]
            node_coordinates.append([Coordinates(x, y) for x in x_coordinates_of_notes])
        return node_coordinates

    def _create_node_with_neighbors(self, coordinate: Coordinates) -> Node:
        node = Node(self._screen_coordinates_associated_with(coordinate))
        self._set_horizontal_neighbors(coordinate, node)
        self._set_vertical_neighbors(coordinate, node)
        self._nodes.append(node)
        if coordinate.x == len(self._maze_lines[0]) - 1:
            portal_neighbor = self._node_associated_with(Coordinates(0, coordinate.y))
            node.set_neighbor(portal_neighbor, NeighborType.PORTAL)
            portal_neighbor.set_neighbor(node, NeighborType.PORTAL)
        return node

    def _set_vertical_neighbors(self, coordinate: Coordinates, node: Node) -> None:
        if self._node_has_upper_connection(coordinate):
            neighbor = self._find_upper_neighbor(coordinate)
            node.set_neighbor(neighbor, NeighborType.UP)
            neighbor.set_neighbor(node, NeighborType.DOWN)

    def _set_horizontal_neighbors(self, coordinate: Coordinates, node: Node) -> None:
        if self._node_has_left_connection(coordinate):
            neighbor = self._find_left_neighbor(coordinate)
            node.set_neighbor(neighbor, NeighborType.LEFT)
            neighbor.set_neighbor(node, NeighborType.RIGHT)

    def _node_has_left_connection(self, coordinate: Coordinates) -> bool:
        line = self._maze_lines[coordinate.y]
        return coordinate.x > 0 and line[coordinate.x - 1] == PELLET_SYMBOL

    def _node_has_upper_connection(self, coordinate: Coordinates) -> bool:
        line = self._transposed_maze_lines[coordinate.x]
        return coordinate.y > 0 and line[coordinate.y - 1] == PELLET_SYMBOL

    def _find_left_neighbor(self, coordinate: Coordinates) -> Node:
        line = self._maze_lines[coordinate.y]
        x = coordinate.x - 1
        while not line[x] == NODE_WITH_PELLET_SYMBOL:
            x -= 1

        return self._node_associated_with(Coordinates(x, coordinate.y))

    def _find_upper_neighbor(self, coordinate: Coordinates) -> Node:
        line = self._transposed_maze_lines[coordinate.x]
        y = coordinate.y - 1
        while not line[y] == NODE_WITH_PELLET_SYMBOL:
            y -= 1

        return self._node_associated_with(Coordinates(coordinate.x, y))

    @staticmethod
    def _screen_coordinates_associated_with(coordinate: Coordinates) -> Coordinates:
        return Coordinates(coordinate.x * TILEWIDTH, coordinate.y * TILEHEIGHT)

    def _node_associated_with(self, coordinate: Coordinates) -> Node:
        screen_coordinates = self._screen_coordinates_associated_with(coordinate)
        return [node for node in self._nodes
                if node.coordinates.x == screen_coordinates.x and node.coordinates.y == screen_coordinates.y][0]
