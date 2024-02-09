import pytest
from hamcrest import assert_that, is_

from src.coordinates import Coordinates
from src.game_event import Command
from src.direction import Direction
from src.node import Node
from src.pacman import Pacman
from src.ports.screen import Screen
from .adapters.fake_screen import FakeScreen
from .screen_observer import FakeScreenObserver


class TestPacman:
    _screen_observer = None

    @pytest.fixture
    def a_node(self):
        return Node(Coordinates(80, 80))

    @pytest.fixture
    def one_neighbor_node(self):
        a_node = Node(Coordinates(80, 80))
        neighbor = Node(Coordinates(80, 70))
        a_node.set_neighbor(neighbor, Direction.UP)
        return a_node

    @pytest.fixture(autouse=True)
    def screen_observer(self):
        self._screen_observer = FakeScreenObserver()

    @pytest.fixture
    def screen(self) -> Screen:
        return FakeScreen(self._screen_observer)

    def test_move_pacman_on_single_node_without_neighbors(self, screen, a_node):
        pacman = Pacman(a_node)
        pacman.update(Command(Direction.UP), 0.01)
        pacman.render(screen)
        assert_that(len(self._screen_observer.messages), is_(1))
        assert_that(self._screen_observer.messages[0], is_('Circle with radius 10 rendered at <80, 80>'))

    def test_move_pacman_one_step_from_single_node_with_neighbor(self, screen, one_neighbor_node):
        pacman = Pacman(one_neighbor_node)

        pacman.update(Command(Direction.UP), 0.01)
        pacman.render(screen)
        assert_that(len(self._screen_observer.messages), is_(1))
        assert_that(self._screen_observer.messages[0], is_('Circle with radius 10 rendered at <80, 79>'))

    def test_move_pacman_two_steps_from_node_with_neighbor(self, screen, one_neighbor_node):
        pacman = Pacman(one_neighbor_node)

        pacman.update(Command(Direction.UP), 0.01)
        pacman.update(Command(Direction.UP), 0.03)
        pacman.render(screen)
        assert_that(len(self._screen_observer.messages), is_(1))
        assert_that(self._screen_observer.messages[0], is_('Circle with radius 10 rendered at <80, 76>'))

    def test_pacman_cannot_move_beyond_target(self, screen, one_neighbor_node):
        pacman = Pacman(one_neighbor_node)

        pacman.update(Command(Direction.UP), 0.09)
        pacman.update(Command(Direction.UP), 0.08)
        pacman.render(screen)
        assert_that(len(self._screen_observer.messages), is_(1))
        assert_that(self._screen_observer.messages[0], is_('Circle with radius 10 rendered at <80, 71>'))

    def test_pacman_may_not_depart_from_road(self, screen, one_neighbor_node):
        pacman = Pacman(one_neighbor_node)

        pacman.update(Command(Direction.UP), 0.03)
        pacman.update(Command(Direction.NONE), 0.02)
        pacman.update(Command(Direction.LEFT), 0.02)
        pacman.render(screen)
        assert_that(len(self._screen_observer.messages), is_(1))
        assert_that(self._screen_observer.messages[0], is_('Circle with radius 10 rendered at <80, 77>'))

    def test_pacman_stops_when_key_released(self, screen, one_neighbor_node):
        pacman = Pacman(one_neighbor_node)

        pacman.update(Command(Direction.UP), 0.01)
        pacman.update(Command(Direction.UP), 0.02)
        pacman.update(Command(Direction.NONE), 0.02)
        pacman.render(screen)
        assert_that(len(self._screen_observer.messages), is_(1))
        assert_that(self._screen_observer.messages[0], is_('Circle with radius 10 rendered at <80, 77>'))

    def test_pacman_may_reverse_direction(self, screen, one_neighbor_node):
        pacman = Pacman(one_neighbor_node)

        pacman.update(Command(Direction.UP), 0.08)
        pacman.update(Command(Direction.NONE), 0.02)
        pacman.update(Command(Direction.DOWN), 0.03)
        pacman.render(screen)
        assert_that(len(self._screen_observer.messages), is_(1))
        assert_that(self._screen_observer.messages[0], is_('Circle with radius 10 rendered at <80, 75>'))

    def test_switch_start_and_target_after_reverse_direction(self, screen, one_neighbor_node):
        pacman = Pacman(one_neighbor_node)

        pacman.update(Command(Direction.UP), 0.03)
        pacman.update(Command(Direction.NONE), 0.02)
        pacman.update(Command(Direction.DOWN), 0.01)
        pacman.update(Command(Direction.DOWN), 0.05)
        pacman.render(screen)
        assert_that(len(self._screen_observer.messages), is_(1))
        assert_that(self._screen_observer.messages[0], is_('Circle with radius 10 rendered at <80, 80>'))
