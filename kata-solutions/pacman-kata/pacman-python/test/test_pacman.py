import pytest
from hamcrest import assert_that, is_

from src.coordinates import Coordinates, PROXIMITY_TOLERANCE
from src.direction import Direction
from src.pellet_group import PelletGroup
from src.position_on_vertex import PositionOnVertex
from src.sprites.node import Node, NeighborType
from src.sprites.pacman import Pacman, PACMAN_RADIUS, COLLISION_RADIUS
from src.ports.screen import Screen
from src.sprites.pellet import Pellet, PelletPoints
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
        a_node.set_neighbor(neighbor, NeighborType.UP)
        return a_node

    @pytest.fixture(autouse=True)
    def screen_observer(self):
        self._screen_observer = FakeScreenObserver()

    @pytest.fixture
    def screen(self) -> Screen:
        return FakeScreen(self._screen_observer)

    def test_move_pacman_on_single_node_without_neighbors(self, screen, a_node):
        pacman = Pacman(PositionOnVertex(a_node))
        pacman.move(Direction.UP, 0.01)
        pacman.render(screen)
        assert_that(len(self._screen_observer.messages), is_(1))
        assert_that(self._screen_observer.messages[0], is_(
            f'Circle with radius {PACMAN_RADIUS} rendered at <80, 80>'))

    def test_move_pacman_one_step_from_single_node_with_neighbor(self, screen, one_neighbor_node):
        pacman = Pacman(PositionOnVertex(one_neighbor_node))

        pacman.move(Direction.UP, 0.01)
        pacman.render(screen)
        assert_that(len(self._screen_observer.messages), is_(1))
        assert_that(self._screen_observer.messages[0], is_(
            f'Circle with radius {PACMAN_RADIUS} rendered at <80, 79>'))

    def test_move_pacman_two_steps_from_node_with_neighbor(self, screen, one_neighbor_node):
        pacman = Pacman(PositionOnVertex(one_neighbor_node))

        pacman.move(Direction.UP, 0.01)
        pacman.move(Direction.UP, 0.03)
        pacman.render(screen)
        assert_that(len(self._screen_observer.messages), is_(1))
        assert_that(self._screen_observer.messages[0], is_(
            f'Circle with radius {PACMAN_RADIUS} rendered at <80, 76>'))

    def test_pacman_cannot_move_beyond_target(self, screen, one_neighbor_node):
        pacman = Pacman(PositionOnVertex(one_neighbor_node))

        pacman.move(Direction.UP, 0.09)
        pacman.move(Direction.UP, 0.08)
        pacman.render(screen)
        assert_that(len(self._screen_observer.messages), is_(1))
        assert_that(self._screen_observer.messages[0], is_(
            f'Circle with radius {PACMAN_RADIUS} rendered at <80, 71>'))

    def test_pacman_may_not_depart_from_road(self, screen, one_neighbor_node):
        pacman = Pacman(PositionOnVertex(one_neighbor_node))

        pacman.move(Direction.UP, 0.03)
        pacman.move(Direction.NONE, 0.02)
        pacman.move(Direction.LEFT, 0.02)
        pacman.render(screen)
        assert_that(len(self._screen_observer.messages), is_(1))
        assert_that(self._screen_observer.messages[0], is_(
            f'Circle with radius {PACMAN_RADIUS} rendered at <80, 77>'))

    def test_pacman_stops_when_key_released(self, screen, one_neighbor_node):
        pacman = Pacman(PositionOnVertex(one_neighbor_node))

        pacman.move(Direction.UP, 0.01)
        pacman.move(Direction.UP, 0.02)
        pacman.move(Direction.NONE, 0.02)
        pacman.render(screen)
        assert_that(len(self._screen_observer.messages), is_(1))
        assert_that(self._screen_observer.messages[0], is_(
            f'Circle with radius {PACMAN_RADIUS} rendered at <80, 77>'))

    def test_pacman_may_reverse_direction(self, screen, one_neighbor_node):
        pacman = Pacman(PositionOnVertex(one_neighbor_node))

        pacman.move(Direction.UP, PROXIMITY_TOLERANCE * .01 + 0.03)
        pacman.move(Direction.DOWN, 0.02)
        pacman.render(screen)

        expected_coordinates = Coordinates(80, 80 - PROXIMITY_TOLERANCE - 0.03 + 0.02)
        assert_that(len(self._screen_observer.messages), is_(1))
        assert_that(self._screen_observer.messages[0], is_(
            f'Circle with radius {PACMAN_RADIUS} rendered at {expected_coordinates}'))

    def test_switch_start_and_target_after_reverse_direction(self, screen, one_neighbor_node):
        pacman = Pacman(PositionOnVertex(one_neighbor_node))

        pacman.move(Direction.UP, PROXIMITY_TOLERANCE * .01 + 0.03)
        pacman.move(Direction.DOWN, 0.05)
        pacman.move(Direction.DOWN, 0.05)
        pacman.render(screen)
        assert_that(len(self._screen_observer.messages), is_(1))
        assert_that(self._screen_observer.messages[0], is_(
            f'Circle with radius {PACMAN_RADIUS} rendered at <80, 79>'))

    def test_arrived_at_target_pacman_changes_direction(self, one_neighbor_node, screen):
        one_neighbor_node.neighbor_at(Direction.UP).set_neighbor(Node(Coordinates(90, 70)), NeighborType.RIGHT)
        pacman = Pacman(PositionOnVertex(one_neighbor_node))

        pacman.move(Direction.UP, 0.09)
        pacman.move(Direction.RIGHT, 0.05)
        pacman.render(screen)
        assert_that(len(self._screen_observer.messages), is_(1))
        assert_that(self._screen_observer.messages[0], is_(
            f'Circle with radius {PACMAN_RADIUS} rendered at <85, 70>'))

    def test_pacman_continues_moving_in_same_direction(self, one_neighbor_node, screen):
        pacman = Pacman(PositionOnVertex(one_neighbor_node))

        pacman.move(Direction.UP, PROXIMITY_TOLERANCE * .01 + 0.01)
        pacman.move(Direction.UP, 0.02)
        pacman.move(Direction.UP, 0.02)
        pacman.render(screen)

        expected_coordinates = Coordinates(80, 80 - PROXIMITY_TOLERANCE - 1 - 2 - 2)
        assert_that(len(self._screen_observer.messages), is_(1))
        assert_that(self._screen_observer.messages[0], is_(
            f'Circle with radius {PACMAN_RADIUS} rendered at {expected_coordinates}'))

    def test_pacman_moves_through_portal(self, screen):
        portal_node_left = Node(Coordinates(100, 100))
        portal_node_right = Node(Coordinates(120, 100))
        middle_node = Node(Coordinates(110, 100))
        middle_node.set_neighbor(portal_node_right, NeighborType.RIGHT)
        middle_node.set_neighbor(portal_node_left, NeighborType.LEFT)
        portal_node_left.set_neighbor(portal_node_right, NeighborType.PORTAL)
        portal_node_left.set_neighbor(middle_node, NeighborType.RIGHT)
        portal_node_right.set_neighbor(portal_node_left, NeighborType.PORTAL)
        portal_node_right.set_neighbor(middle_node, NeighborType.LEFT)

        pacman = Pacman(PositionOnVertex(middle_node))

        pacman.move(Direction.RIGHT, 0.1)
        pacman.move(Direction.RIGHT, 0.05)
        pacman.render(screen)

        expected_coordinates = Coordinates(105, 100)
        assert_that(len(self._screen_observer.messages), is_(1))
        assert_that(self._screen_observer.messages[0], is_(
            f'Circle with radius {PACMAN_RADIUS} rendered at {expected_coordinates}'))

    def test_pacman_cannot_eat_pellet(self):
        start_node = Node(Coordinates(80, 80))
        pellet_coordinates = Coordinates(90, 80)
        pellet_group = PelletGroup([Pellet(pellet_coordinates)])

        pacman = Pacman(PositionOnVertex(start_node))

        assert_that(pellet_group.remove_pellet_when_pacman_is_close(pacman.coordinates), is_(PelletPoints.ZERO))
        assert_that(len(pellet_group.pellets), is_(1))

    def test_pacman_can_eat_pellet(self):
        start_node = Node(Coordinates(80, 80))
        pellet_coordinates = Coordinates(80 + COLLISION_RADIUS - 1, 80)
        pellet_group = PelletGroup([Pellet(pellet_coordinates)])

        pacman = Pacman(PositionOnVertex(start_node))

        assert_that(pellet_group.remove_pellet_when_pacman_is_close(pacman.coordinates), is_(PelletPoints.PELLET))
        assert_that(len(pellet_group.pellets), is_(0))

    def test_pacman_can_eat_power_pellet(self):
        start_node = Node(Coordinates(80, 80))
        pellet_coordinates = Coordinates(80 + COLLISION_RADIUS - 1, 80)
        pellet_group = PelletGroup([Pellet(pellet_coordinates, is_power_pellet=True)])

        pacman = Pacman(PositionOnVertex(start_node))

        assert_that(pellet_group.remove_pellet_when_pacman_is_close(pacman.coordinates), is_(PelletPoints.POWER_PELLET))
        assert_that(len(pellet_group.pellets), is_(0))
