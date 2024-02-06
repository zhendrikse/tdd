from .maze import Maze, PACMAN_MAZE
from .adapters.pygame_screen import PyGameScreen
from .adapters.pygame_eventbus import PyGameEventBus
from .adapters.pygame_clock import PyGameClock
from .game import Game

if __name__ == "__main__":
    nodes = Maze(PACMAN_MAZE).as_node_group()
    game = Game(PyGameEventBus(), PyGameClock(), PyGameScreen(), nodes)
    game.run()
