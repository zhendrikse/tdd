import pytest
from hamcrest import assert_that, is_

from src.coordinates import Coordinates
from src.game_event import Command
from src.node import Node
from src.node_group import NodeGroup
from src.pacman import Pacman
from src.ports.screen import Screen
from .adapters.fake_screen import FakeScreen
from .screen_observer import FakeScreenObserver


class TestPacman:
    _screen_observer = None

    @pytest.fixture(autouse=True)
    def screen_observer(self):
        self._screen_observer = FakeScreenObserver()

    @pytest.fixture
    def screen(self) -> Screen:
        return FakeScreen(self._screen_observer)

    def test_pacman_on_single_node(self, screen):
        nodes = NodeGroup([Node(Coordinates(80, 80))])
        pacman = Pacman(nodes)
        pacman.update(Command.UP, 0.01)
        pacman.render(screen)
        assert_that(len(self._screen_observer.messages), is_(1))
        assert_that(self._screen_observer.messages[0], is_('Circle with radius 10 rendered at <80.0, 79.0>'))
