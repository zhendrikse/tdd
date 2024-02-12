import pytest
from hamcrest import is_, assert_that
from typing import List

from src.coordinates import Coordinates
from src.game import Game
from src.game_event import KeyPress, GameEvent
from src.sprites.node import Node, NeighborType
from src.node_group import NodeGroup

from .adapters.fake_clock import FakeClock
from .adapters.fake_eventbus import FakeEventBus
from .adapters.fake_screen import FakeScreen
from .screen_observer import FakeScreenObserver

QUIT_EVENT = GameEvent(do_quit=True)


class TestGame:
    _screen_observer = None

    @pytest.fixture(autouse=True)
    def screen_observer(self):
        self._screen_observer = FakeScreenObserver()

    def _given_a_game_with_events(self, events: List[List[GameEvent]]) -> Game:
        screen = FakeScreen(self._screen_observer)
        event_bus = FakeEventBus(events)
        a_node = Node(Coordinates(80, 80))

        right_neighbor = Node(Coordinates(100, 80))
        left_neighbor = Node(Coordinates(60, 80))
        up_neighbor = Node(Coordinates(80, 60))
        down_neighbor = Node(Coordinates(80, 100))

        a_node.set_neighbor(right_neighbor, NeighborType.RIGHT)
        a_node.set_neighbor(left_neighbor, NeighborType.LEFT)
        a_node.set_neighbor(up_neighbor, NeighborType.UP)
        a_node.set_neighbor(down_neighbor, NeighborType.DOWN)

        non_rendered_node_group = NodeGroup(
            [a_node, right_neighbor, left_neighbor, up_neighbor, down_neighbor], render_group=False)
        return Game(event_bus, FakeClock(), screen, non_rendered_node_group)

    @staticmethod
    def _assert_observed_screen_updates(expected_updates: List[str], updates: List[str]) -> None:
        assert_that(len(updates), is_(len(expected_updates)))
        for i in range(len(updates)):
            assert_that(updates[i], is_(expected_updates[i]))

    def test_game_without_events_draws_sprite(self):
        events = [[QUIT_EVENT]]
        expected_updates = [
            'blit',
            'Circle with radius 10 rendered at <80, 80>',
            'update',
            'quit']

        self._given_a_game_with_events(events).run()
        self._assert_observed_screen_updates(expected_updates, self._screen_observer.messages)

    def test_second_tick_leaves_sprite_position_unchanged(self):
        events = [[], [QUIT_EVENT]]
        expected_updates = [
            'blit',
            'Circle with radius 10 rendered at <80, 80>', 'update',
            'blit',
            'Circle with radius 10 rendered at <80, 80>', 'update',
            'quit'
        ]
        self._given_a_game_with_events(events).run()
        self._assert_observed_screen_updates(expected_updates, self._screen_observer.messages)

    def test_move_sprite_to_the_right(self):
        events = [
            [GameEvent(keypress=KeyPress.ARROW_RIGHT_PRESSED)],
            [],
            [],
            [GameEvent(keypress=KeyPress.ARROW_RIGHT_RELEASED)],
            [],
            [QUIT_EVENT]]
        expected_updates = [
            'blit', 'Circle with radius 10 rendered at <80, 80>', 'update',
            'blit', 'Circle with radius 10 rendered at <84, 80>', 'update',
            'blit', 'Circle with radius 10 rendered at <88, 80>', 'update',
            'blit', 'Circle with radius 10 rendered at <92, 80>', 'update',
            'blit', 'Circle with radius 10 rendered at <92, 80>', 'update',
            'blit', 'Circle with radius 10 rendered at <92, 80>', 'update',
            'quit'
        ]
        self._given_a_game_with_events(events).run()
        self._assert_observed_screen_updates(expected_updates, self._screen_observer.messages)

    def test_move_sprite_to_the_left(self):
        events = [
            [GameEvent(keypress=KeyPress.ARROW_LEFT_PRESSED)],
            [],
            [],
            [GameEvent(keypress=KeyPress.ARROW_LEFT_RELEASED)],
            [],
            [QUIT_EVENT]]
        expected_updates = [
            'blit', 'Circle with radius 10 rendered at <80, 80>', 'update',
            'blit', 'Circle with radius 10 rendered at <76, 80>', 'update',
            'blit', 'Circle with radius 10 rendered at <72, 80>', 'update',
            'blit', 'Circle with radius 10 rendered at <68, 80>', 'update',
            'blit', 'Circle with radius 10 rendered at <68, 80>', 'update',
            'blit', 'Circle with radius 10 rendered at <68, 80>', 'update',
            'quit'
        ]
        self._given_a_game_with_events(events).run()
        self._assert_observed_screen_updates(expected_updates, self._screen_observer.messages)

    def test_move_sprite_up(self):
        events = [
            [GameEvent(keypress=KeyPress.ARROW_UP_PRESSED)],
            [],
            [],
            [GameEvent(keypress=KeyPress.ARROW_UP_RELEASED)],
            [],
            [QUIT_EVENT]]
        expected_updates = [
            'blit', 'Circle with radius 10 rendered at <80, 80>', 'update',
            'blit', 'Circle with radius 10 rendered at <80, 76>', 'update',
            'blit', 'Circle with radius 10 rendered at <80, 72>', 'update',
            'blit', 'Circle with radius 10 rendered at <80, 68>', 'update',
            'blit', 'Circle with radius 10 rendered at <80, 68>', 'update',
            'blit', 'Circle with radius 10 rendered at <80, 68>', 'update',
            'quit'
        ]
        self._given_a_game_with_events(events).run()
        self._assert_observed_screen_updates(expected_updates, self._screen_observer.messages)

    def test_move_sprite_down(self):
        events = [
            [GameEvent(keypress=KeyPress.ARROW_DOWN_PRESSED)],
            [],
            [],
            [GameEvent(keypress=KeyPress.ARROW_DOWN_RELEASED)],
            [],
            [QUIT_EVENT]]
        expected_updates = [
            'blit', 'Circle with radius 10 rendered at <80, 80>', 'update',
            'blit', 'Circle with radius 10 rendered at <80, 84>', 'update',
            'blit', 'Circle with radius 10 rendered at <80, 88>', 'update',
            'blit', 'Circle with radius 10 rendered at <80, 92>', 'update',
            'blit', 'Circle with radius 10 rendered at <80, 92>', 'update',
            'blit', 'Circle with radius 10 rendered at <80, 92>', 'update',
            'quit'
        ]
        self._given_a_game_with_events(events).run()
        self._assert_observed_screen_updates(expected_updates, self._screen_observer.messages)
