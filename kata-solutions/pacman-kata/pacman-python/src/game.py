import random

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
from .position_on_vertex import PositionOnVertex
from .sprites.ghost import Ghost


class Game:

    def __init__(self, eventbus: EventBus, clock: Clock, screen: Screen, maze: Maze = GameMaze(PACMAN_MAZE)) -> None:
        self._eventbus: EventBus = eventbus
        self._clock: Clock = clock
        self._screen: Screen = screen
        self._nodes: NodeGroup = maze.as_node_group()
        self._pellets: PelletGroup = maze.as_pellet_group()
        start_node = Node(Coordinates(200, 400)) if self._nodes.is_empty() else self._nodes.first()
        self._pacman: Pacman = Pacman(PositionOnVertex(start_node))
        self._ghost: Ghost = Ghost(PositionOnVertex(start_node))

    def run(self) -> None:
        keep_running = True
        pacman_direction = Direction.NONE
        ghost_direction = Direction.NONE
        clock_ticks = 0

        while keep_running:
            clock_ticks += 1
            dt = self._clock.tick(30) / 1000.0

            if clock_ticks % 25 == 0:
                ghost_direction = random.choice(list(Direction))
            self._ghost.move(ghost_direction, dt)

            self._pacman.move(pacman_direction, dt)
            pellet_points = self._pellets.remove_pellet_when_pacman_is_close(self._pacman.coordinates).value

            self._render()

            for event in self._eventbus.get_events():
                pacman_direction = event.as_command()
                if event.is_quit():
                    keep_running = False

        self._screen.quit()

    def _render(self) -> None:
        self._screen.blit()
        self._nodes.render(self._screen)
        self._pellets.render(self._screen)
        self._pacman.render(self._screen)
        self._ghost.render(self._screen)
        self._screen.update()



