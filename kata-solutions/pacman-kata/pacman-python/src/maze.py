from dataclasses import dataclass, field
from typing import List

from .coordinates import Coordinates
from .node import Node, NeighborType
from .node_group import NodeGroup
from .pellet import Pellet
from .pellet_group import PelletGroup
from .ports.screen import TILEHEIGHT, TILEWIDTH

NODE_WITH_PELLET_SYMBOL = "+"
NODE_WITH_POWER_PELLET_SYMBOL = "P"
NODE_WITHOUT_PELLET_SYMBOL = "n"
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
X + . . . . n X X n - - n - - n - - n X X + . . . . + X
X X X X X X | X X | X X . X X . X X | X X . X X X X X X
X X X X X X | X X | X X . X X . X X | X X . X X X X X X
n - - - - - + - - n X X X X X X X X n - - + - - - - - n
X X X X X X . X X | X X X X X X X X | X X . X X X X X X
X X X X X X . X X | X X X X X X X X | X X . X X X X X X
X X X X X X . X X + - - - - - - - - + X X . X X X X X X
X X X X X X . X X | X X X X X X X X | X X . X X X X X X
X X X X X X . X X | X X X X X X X X | X X . X X X X X X
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
    def _dimension_x(self):
        return len(self._maze_lines[0])

    @property
    def _dimension_y(self):
        return len(self._maze_lines)

    @property
    def _transposed_maze_lines(self) -> List[List[str]]:
        return [[self._maze_lines[j][i] for j in range(self._dimension_y)] for i in range(self._dimension_x)]

    @staticmethod
    def _is_connection_symbol(char) -> bool:
        return char in [H_CONNECTION_WITHOUT_PELLET_SYMBOL,
                        V_CONNECTION_WITHOUT_PELLET_SYMBOL,
                        POWER_PELLET_SYMBOL,
                        PELLET_SYMBOL]

    @staticmethod
    def _is_node_symbol(char) -> bool:
        return char in [NODE_WITH_PELLET_SYMBOL,
                        NODE_WITH_POWER_PELLET_SYMBOL,
                        NODE_WITHOUT_PELLET_SYMBOL]

    @staticmethod
    def _is_pellet_symbol(char) -> bool:
        return char in [NODE_WITH_PELLET_SYMBOL,
                        NODE_WITH_POWER_PELLET_SYMBOL,
                        PELLET_SYMBOL,
                        POWER_PELLET_SYMBOL]

    @staticmethod
    def _is_power_pellet_symbol(char) -> bool:
        return char in [NODE_WITH_POWER_PELLET_SYMBOL,
                        POWER_PELLET_SYMBOL]

    def as_pellet_group(self) -> PelletGroup:
        if (NODE_WITH_PELLET_SYMBOL not in self._maze_as_string or
                PELLET_SYMBOL not in self._maze_as_string or
                POWER_PELLET_SYMBOL not in self._maze_as_string or
                NODE_WITH_POWER_PELLET_SYMBOL not in self._maze_as_string):
            return PelletGroup([])

        pellets = [self._create_pellet(pellet_coordinate)
                   for pellet_coordinate in self._determine_coordinates(self._is_pellet_symbol)]

        return PelletGroup(pellets)

    def as_node_group(self) -> NodeGroup:
        if (NODE_WITH_PELLET_SYMBOL not in self._maze_as_string and
                NODE_WITHOUT_PELLET_SYMBOL not in self._maze_as_string and
                NODE_WITH_POWER_PELLET_SYMBOL not in self._maze_as_string):
            return NodeGroup([])

        nodes = [self._create_node_with_neighbors(node_coordinate)
             for node_coordinate in self._determine_coordinates(self._is_node_symbol)]

        return NodeGroup(nodes)

    def _create_pellet(self, coordinate: Coordinates) -> Pellet:
        pellet_symbol = self._maze_lines[coordinate.y][coordinate.x]
        return Pellet(coordinate, self._is_power_pellet_symbol(pellet_symbol))

    def _determine_coordinates(self, symbol_selector) -> List[Coordinates]:
        node_coordinates = [
            [Coordinates(x, y) for x in [
                x for x, char in enumerate(self._maze_lines[y]) if symbol_selector(char)]
             ] for y in range(len(self._maze_lines))]
        flattened_list = [coordinate for node_list in node_coordinates for coordinate in node_list]
        return flattened_list

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
        return coordinate.x > 0 and self._is_connection_symbol(line[coordinate.x - 1])

    def _node_has_upper_connection(self, coordinate: Coordinates) -> bool:
        line = self._transposed_maze_lines[coordinate.x]
        return coordinate.y > 0 and self._is_connection_symbol(line[coordinate.y - 1])

    def _find_left_neighbor(self, coordinate: Coordinates) -> Node:
        line = self._maze_lines[coordinate.y]
        x = coordinate.x - 1
        while not self._is_node_symbol(line[x]):
            x -= 1

        return self._node_associated_with(Coordinates(x, coordinate.y))

    def _find_upper_neighbor(self, coordinate: Coordinates) -> Node:
        line = self._transposed_maze_lines[coordinate.x]
        y = coordinate.y - 1
        while not self._is_node_symbol(line[y]):
            y -= 1

        return self._node_associated_with(Coordinates(coordinate.x, y))

    @staticmethod
    def _screen_coordinates_associated_with(coordinate: Coordinates) -> Coordinates:
        return Coordinates(coordinate.x * TILEWIDTH, coordinate.y * TILEHEIGHT)

    def _node_associated_with(self, coordinate: Coordinates) -> Node:
        screen_coordinates = self._screen_coordinates_associated_with(coordinate)
        return [node for node in self._nodes
                if node.coordinates.x == screen_coordinates.x and node.coordinates.y == screen_coordinates.y][0]
