from .coordinates import Coordinates
from .direction import Direction
from .node import Node
from .sprite import Sprite
from .node_group import NodeGroup
from .ports.eventbus import EventBus
from .ports.clock import Clock
from .ports.screen import Screen
from .pacman import Pacman
from .game_event import Command


class Game:

    def __init__(self, eventbus: EventBus, clock: Clock, screen: Screen, nodes: NodeGroup = NodeGroup([])) -> None:
        self._eventbus = eventbus
        self._clock = clock
        self._screen = screen
        self._nodes: NodeGroup = nodes
        start_node = Node(Coordinates(200, 400)) if nodes.is_empty() else nodes.first()
        self._pacman: Sprite = Pacman(start_node)

    def run(self) -> None:
        keep_running = True
        command = Command(Direction.NONE)

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
        self._pacman.render(self._screen)
        self._screen.update()



