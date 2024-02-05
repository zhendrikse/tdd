from .coordinates import Coordinates
from .node import Node
from .direction import Direction
from .adapters.pygame_screen import PyGameScreen
from .adapters.pygame_eventbus import PyGameEventBus
from .adapters.pygame_clock import PyGameClock
from .game import Game
from .node_group import NodeGroup

node_a = Node(Coordinates(80, 80))
node_b = Node(Coordinates(160, 80))
node_c = Node(Coordinates(80, 160))
node_d = Node(Coordinates(160, 160))
node_e = Node(Coordinates(208, 160))
node_f = Node(Coordinates(80, 320))
node_g = Node(Coordinates(208, 320))
node_a.set_neighbor(node_b, Direction.RIGHT)
node_a.set_neighbor(node_c, Direction.DOWN)
node_b.set_neighbor(node_a, Direction.LEFT)
node_b.set_neighbor(node_d, Direction.DOWN)
node_c.set_neighbor(node_a, Direction.UP)
node_c.set_neighbor(node_d, Direction.RIGHT)
node_c.set_neighbor(node_f, Direction.DOWN)
node_d.set_neighbor(node_b, Direction.UP)
node_d.set_neighbor(node_c, Direction.LEFT)
node_d.set_neighbor(node_e, Direction.RIGHT)
node_e.set_neighbor(node_d, Direction.LEFT)
node_e.set_neighbor(node_g, Direction.DOWN)
node_f.set_neighbor(node_c, Direction.UP)
node_f.set_neighbor(node_g, Direction.RIGHT)
node_g.set_neighbor(node_e, Direction.UP)
node_g.set_neighbor(node_f, Direction.LEFT)

if __name__ == "__main__":
    nodes = NodeGroup([node_a, node_b, node_c, node_d, node_e, node_f, node_g])
    game = Game(PyGameEventBus(), PyGameClock(), PyGameScreen(), nodes)
    game.run()
