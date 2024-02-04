import pytest

from hamcrest import is_, assert_that, has_length
from typing import List

from src.coordinates import Coordinates
from src.game import Game
from src.node import Node, Orientation
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
        return NodeGroup([node_a, node_b, node_c, node_d, node_e, node_f, node_g])

    def test_render_single_node(self, screen):
        Node(Coordinates(80, 90)).render(screen)
        assert_that(len(self._screen_observer.messages), is_(1))
        assert_that(self._screen_observer.messages[0], is_('Circle with radius 12 rendered at <80, 90>'))

    def test_render_two_connected_nodes(self, screen):
        node1 = Node(Coordinates(60, 70))
        node2 = Node(Coordinates(60, 90))
        node1.set_neighbor(node2, Orientation.DOWN)
        node1.render(screen)
        assert_that(len(self._screen_observer.messages), is_(2))
        assert_that(self._screen_observer.messages[0], is_('Circle with radius 12 rendered at <60, 70>'))
        assert_that(self._screen_observer.messages[1], is_('Line between <60, 70> and <60, 90> with width=4'))

    def test_render_node_group(self, test_node_group, screen):
        test_node_group.render(screen)
        assert_that(len(self._screen_observer.messages), is_(23))
