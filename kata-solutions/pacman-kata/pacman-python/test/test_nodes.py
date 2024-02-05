import pytest

from hamcrest import is_, assert_that, has_length
from typing import List

from src.coordinates import Coordinates
from src.direction import Direction
from src.node import Node
from src.node_group import NodeGroup
from src.ports.screen import Screen
from .adapters.fake_screen import FakeScreen
from .screen_observer import FakeScreenObserver


class TestNodes:
    _screen_observer = None

    @pytest.fixture(autouse=True)
    def screen_observer(self):
        self._screen_observer = FakeScreenObserver()

    @pytest.fixture
    def screen(self) -> Screen:
        return FakeScreen(self._screen_observer)

    @pytest.fixture()
    def test_node_group(self) -> NodeGroup:
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
        return NodeGroup([node_a, node_b, node_c, node_d, node_e, node_f, node_g])

    def test_render_single_node(self, screen):
        Node(Coordinates(80, 90)).render(screen)
        assert_that(len(self._screen_observer.messages), is_(1))
        assert_that(self._screen_observer.messages[0], is_('Circle with radius 12 rendered at <80, 90>'))

    def test_render_two_connected_nodes(self, screen):
        node1 = Node(Coordinates(60, 70))
        node2 = Node(Coordinates(60, 90))
        node1.set_neighbor(node2, Direction.DOWN)
        node1.render(screen)
        assert_that(len(self._screen_observer.messages), is_(2))
        assert_that(self._screen_observer.messages[0], is_('Circle with radius 12 rendered at <60, 70>'))
        assert_that(self._screen_observer.messages[1], is_('Line between <60, 70> and <60, 90> with width=4'))

    def test_render_node_group(self, test_node_group, screen):
        test_node_group.render(screen)
        assert_that(len(self._screen_observer.messages), is_(23))
