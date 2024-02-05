import pytest

from hamcrest import is_, assert_that, is_not

from src.coordinates import Coordinates
from src.direction import Direction
from src.node import Node
from src.node_group import NodeGroup
from src.ports.screen import Screen, TILEWIDTH
from .adapters.fake_screen import FakeScreen
from .screen_observer import FakeScreenObserver


class TestRenderNodeGroup:
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
        NodeGroup([node1, node2]).render(screen)
        assert_that(len(self._screen_observer.messages), is_(3))
        assert_that(self._screen_observer.messages[0], is_('Circle with radius 12 rendered at <60, 70>'))
        assert_that(self._screen_observer.messages[1], is_('Line between <60, 70> and <60, 90> with width=4'))
        assert_that(self._screen_observer.messages[2], is_('Circle with radius 12 rendered at <60, 90>'))

    def test_render_node_group(self, test_node_group, screen):
        test_node_group.render(screen)
        assert_that(len(self._screen_observer.messages), is_(23))


class TestCreateNodeGroup:
    _screen_observer = None

    @pytest.fixture(autouse=True)
    def screen_observer(self):
        self._screen_observer = FakeScreenObserver()

    @pytest.fixture
    def screen(self) -> Screen:
        return FakeScreen(self._screen_observer)

    def test_node_group_from_emtpy_string(self):
        assert_that(NodeGroup.from_string("").is_empty(), is_(True))

    def test_node_group_from_emtpy_space_symbols_string(self):
        assert_that(NodeGroup.from_string("XXXX").is_empty(), is_(True))

    def test_single_node_node_group(self):
        nodes = NodeGroup.from_string("+")
        assert_that(nodes.is_empty(), is_(False))
        assert_that(nodes.first(), is_not(None))
        assert_that(nodes.first().coordinates, is_(Coordinates(0, 0)))

    def test_single_node_node_group_with_trailing_spaces(self):
        nodes = NodeGroup.from_string("+ X X")
        assert_that(nodes.is_empty(), is_(False))
        assert_that(nodes.first(), is_not(None))
        assert_that(nodes.first().coordinates, is_(Coordinates(0, 0)))

    def test_single_node_node_group_with_leading_spaces(self):
        nodes = NodeGroup.from_string("X X + X X")
        assert_that(nodes.is_empty(), is_(False))
        assert_that(nodes.first(), is_not(None))
        assert_that(nodes.first().coordinates, is_(Coordinates(TILEWIDTH * 2, 0)))

    def test_unconnected_double_nodes_node_group(self, screen):
        nodes = NodeGroup.from_string("X + X X + X X X")
        nodes.render(screen)

        assert_that(len(self._screen_observer.messages), is_(2))
        assert_that(self._screen_observer.messages[0], is_("Circle with radius 12 rendered at <16, 0>"))
        assert_that(self._screen_observer.messages[1], is_("Circle with radius 12 rendered at <64, 0>"))

    def test_connected_double_nodes_node_group(self, screen):
        nodes = NodeGroup.from_string("X + . . + X X X")
        nodes.render(screen)

        assert_that(len(self._screen_observer.messages), is_(4))
        assert_that(self._screen_observer.messages[0], is_("Circle with radius 12 rendered at <16, 0>"))
        assert_that(self._screen_observer.messages[1], is_("Line between <16, 0> and <64, 0> with width=4"))
        assert_that(self._screen_observer.messages[2], is_("Circle with radius 12 rendered at <64, 0>"))
        assert_that(self._screen_observer.messages[3], is_("Line between <64, 0> and <16, 0> with width=4"))

    def test_connected_double_nodes_node_group_starting_on_second_line(self, screen):
        nodes = NodeGroup.from_string("X X X X X X X X\n" + "X + . . + X X X")
        nodes.render(screen)

        assert_that(len(self._screen_observer.messages), is_(4))
        assert_that(self._screen_observer.messages[0], is_("Circle with radius 12 rendered at <16, 16>"))
        assert_that(self._screen_observer.messages[1], is_("Line between <16, 16> and <64, 16> with width=4"))
        assert_that(self._screen_observer.messages[2], is_("Circle with radius 12 rendered at <64, 16>"))
        assert_that(self._screen_observer.messages[3], is_("Line between <64, 16> and <16, 16> with width=4"))

    # def test_node_group_from_string(self):
    #     text_based_node_group = \
    #         "X X X X X X X X\n" + \
    #         "X + . . + X X X\n" + \
    #         "X . X X . X X X\n" + \
    #         "X + . . + . + X\n" + \
    #         "X . X X X X . X\n" + \
    #         "X . X X X X . X\n" + \
    #         "X + . . . . + X\n" + \
    #         "X X X X X X X X\n"
    #
    #     assert_that(NodeGroup.from_string(text_based_node_group), is_(NodeGroup([])))
