from .sprite import Sprite
from .node_group import NodeGroup
from .ports.eventbus import EventBus
from .ports.clock import Clock
from .ports.screen import Screen
from .pacman import Pacman
from .game_event import Command


class Game:

    def __init__(self, eventbus: EventBus, clock: Clock, screen: Screen) -> None:
        self._eventbus = eventbus
        self._clock = clock
        self._screen = screen
        self._nodes: NodeGroup = NodeGroup([])
        self._pacman: Sprite = Pacman(self._nodes)

    def start(self, nodes: NodeGroup = NodeGroup([])) -> None:
        self._screen.set_background()
        self._pacman = Pacman(nodes)
        self._nodes = nodes

    def run(self) -> None:
        keep_running = True
        direction = Command.STOP

        while keep_running:
            dt = self._clock.tick(30) / 1000.0
            self._render(direction, dt)
            for event in self._eventbus.get_events():
                #  print(f"Received event {event}, direction is now {direction}")
                if event.is_arrow_key():
                    direction = event.as_command()
                if event.is_quit():
                    keep_running = False

        self._screen.quit()

    def _render(self, command: Command, dt: float) -> None:
        # print(f"Rendering with command={command} and dt={dt}")
        self._pacman.update(command, dt)

        self._screen.blit()
        self._nodes.render(self._screen)
        self._pacman.render(self._screen)
        self._screen.update()



