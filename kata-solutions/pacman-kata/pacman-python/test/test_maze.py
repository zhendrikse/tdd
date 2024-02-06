import pytest

from hamcrest import is_, assert_that, is_not

from src.coordinates import Coordinates
from src.maze import Maze
from src.ports.screen import Screen, TILEWIDTH
from .adapters.fake_screen import FakeScreen
from .screen_observer import FakeScreenObserver


class TestMaze:
    _screen_observer = None

    @pytest.fixture(autouse=True)
    def screen_observer(self):
        self._screen_observer = FakeScreenObserver()

    @pytest.fixture
    def screen(self) -> Screen:
        return FakeScreen(self._screen_observer)

    def test_node_group_from_emtpy_string(self):
        assert_that(Maze("").as_node_group().is_empty(), is_(True))

    def test_node_group_from_emtpy_space_symbols_string(self):
        assert_that(Maze("XXXX").as_node_group().is_empty(), is_(True))

    def test_single_node_node_group(self):
        nodes = Maze("+").as_node_group()
        assert_that(nodes.is_empty(), is_(False))
        assert_that(nodes.first(), is_not(None))
        assert_that(nodes.first().coordinates, is_(Coordinates(0, 0)))

    def test_single_node_node_group_with_trailing_spaces(self):
        nodes = Maze("+ X X").as_node_group()
        assert_that(nodes.is_empty(), is_(False))
        assert_that(nodes.first(), is_not(None))
        assert_that(nodes.first().coordinates, is_(Coordinates(0, 0)))

    def test_single_node_node_group_with_leading_spaces(self):
        nodes = Maze("X X + X X").as_node_group()
        assert_that(nodes.is_empty(), is_(False))
        assert_that(nodes.first(), is_not(None))
        assert_that(nodes.first().coordinates, is_(Coordinates(TILEWIDTH * 2, 0)))

    def test_unconnected_double_nodes_node_group(self, screen):
        nodes = Maze("X + X X + X X X").as_node_group()
        nodes.render(screen)

        assert_that(len(self._screen_observer.messages), is_(2))
        assert_that(self._screen_observer.messages[0], is_("Circle with radius 12 rendered at <16, 0>"))
        assert_that(self._screen_observer.messages[1], is_("Circle with radius 12 rendered at <64, 0>"))

    def test_connected_double_nodes_node_group(self, screen):
        nodes = Maze("X + . . + X X X").as_node_group()
        nodes.render(screen)

        assert_that(len(self._screen_observer.messages), is_(4))
        assert_that(self._screen_observer.messages[0], is_("Circle with radius 12 rendered at <16, 0>"))
        assert_that(self._screen_observer.messages[1], is_("Line between <16, 0> and <64, 0> with width=4"))
        assert_that(self._screen_observer.messages[2], is_("Circle with radius 12 rendered at <64, 0>"))
        assert_that(self._screen_observer.messages[3], is_("Line between <64, 0> and <16, 0> with width=4"))

    def test_connected_double_nodes_node_group_starting_on_second_line(self, screen):
        nodes = Maze("X X X X X X X X\n" + "X + . . + X X X").as_node_group()
        nodes.render(screen)

        assert_that(len(self._screen_observer.messages), is_(4))
        assert_that(self._screen_observer.messages[0], is_("Circle with radius 12 rendered at <16, 16>"))
        assert_that(self._screen_observer.messages[1], is_("Line between <16, 16> and <64, 16> with width=4"))
        assert_that(self._screen_observer.messages[2], is_("Circle with radius 12 rendered at <64, 16>"))
        assert_that(self._screen_observer.messages[3], is_("Line between <64, 16> and <16, 16> with width=4"))

    def test_test_maze(self, screen):
        test_maze = '''X X X X X X X X
X + . . + X X X
X . X X . X X X
X + . . + . + X
X . X X X X . X
X . X X X X . X
X + . . . . + X
X X X X X X X X
'''
        nodes = Maze(test_maze).as_node_group()
        nodes.render(screen)

        assert_that(len(self._screen_observer.messages), is_(23))
        assert_that(self._screen_observer.messages[0], is_("Circle with radius 12 rendered at <16, 16>"))
        assert_that(self._screen_observer.messages[1], is_("Line between <16, 16> and <64, 16> with width=4"))
        assert_that(self._screen_observer.messages[2], is_("Line between <16, 16> and <16, 48> with width=4"))
        assert_that(self._screen_observer.messages[3], is_("Circle with radius 12 rendered at <64, 16>"))
        assert_that(self._screen_observer.messages[4], is_("Line between <64, 16> and <16, 16> with width=4"))
        assert_that(self._screen_observer.messages[5], is_("Line between <64, 16> and <64, 48> with width=4"))
        assert_that(self._screen_observer.messages[6], is_("Circle with radius 12 rendered at <16, 48>"))
        assert_that(self._screen_observer.messages[7], is_("Line between <16, 48> and <16, 16> with width=4"))
        assert_that(self._screen_observer.messages[8], is_("Line between <16, 48> and <64, 48> with width=4"))
        # We leave the remainder of the assertions out
