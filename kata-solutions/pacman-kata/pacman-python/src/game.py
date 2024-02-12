from .coordinates import Coordinates
from .direction import Direction
from src.sprites.node import Node
from .maze import Maze, PACMAN_MAZE, GameMaze
from .node_group import NodeGroup
from .pellet_group import PelletGroup
from .ports.eventbus import EventBus
from .ports.clock import Clock
from .ports.screen import Screen
from src.sprites.pacman import Pacman
from .sprites.movable import Movable


class Game:

    def __init__(self, eventbus: EventBus, clock: Clock, screen: Screen, maze: Maze = GameMaze(PACMAN_MAZE)) -> None:
        self._eventbus: EventBus = eventbus
        self._clock: Clock = clock
        self._screen: Screen = screen
        self._nodes: NodeGroup = maze.as_node_group()
        self._pellets: PelletGroup = maze.as_pellet_group()
        start_node = Node(Coordinates(200, 400)) if self._nodes.is_empty() else self._nodes.first()
        self._pacman: Movable = Pacman(start_node)

    def run(self) -> None:
        keep_running = True
        command = Direction.NONE

        while keep_running:
            dt = self._clock.tick(30) / 1000.0
            self._pacman.move(command, dt)
            self._render()
            for event in self._eventbus.get_events():
                command = event.as_command()
                if event.is_quit():
                    keep_running = False

        self._screen.quit()

    def _render(self) -> None:
        self._screen.blit()
        self._nodes.render(self._screen)
        self._pellets.render(self._screen)
        self._pacman.render(self._screen)
        self._screen.update()



