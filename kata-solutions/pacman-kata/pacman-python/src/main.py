from .coordinates import Coordinates
from .node import Node, Orientation
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
node_a.set_neighbor(node_b, Orientation.RIGHT)
node_a.set_neighbor(node_c, Orientation.DOWN)
node_b.set_neighbor(node_a, Orientation.LEFT)
node_b.set_neighbor(node_d, Orientation.DOWN)
node_c.set_neighbor(node_a, Orientation.UP)
node_c.set_neighbor(node_d, Orientation.RIGHT)
node_c.set_neighbor(node_f, Orientation.DOWN)
node_d.set_neighbor(node_b, Orientation.UP)
node_d.set_neighbor(node_c, Orientation.LEFT)
node_d.set_neighbor(node_e, Orientation.RIGHT)
node_e.set_neighbor(node_d, Orientation.LEFT)
node_e.set_neighbor(node_g, Orientation.DOWN)
node_f.set_neighbor(node_c, Orientation.UP)
node_f.set_neighbor(node_g, Orientation.RIGHT)
node_g.set_neighbor(node_e, Orientation.UP)
node_g.set_neighbor(node_f, Orientation.LEFT)

if __name__ == "__main__":
    game = Game(PyGameEventBus(), PyGameClock(), PyGameScreen())
    game.start(NodeGroup([node_a, node_b, node_c, node_d, node_e, node_f, node_g]))
    game.run()
