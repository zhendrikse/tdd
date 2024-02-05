import pytest
from hamcrest import is_, assert_that, has_length
from typing import List
from src.game import Game
from src.game_event import KeyPress, GameEvent

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
        return Game(event_bus, FakeClock(), screen)

    def _assert_observed_screen_updates(self, expected_updates: List[str], updates: List[str]) -> None:
        assert_that(updates, has_length(len(expected_updates)))
        for i in range(len(updates)):
            assert_that(updates[i], is_(expected_updates[i]))

    def test_game_without_events_draws_sprite(self):
        events = [[QUIT_EVENT]]
        expected_updates = ['Circle with radius 10 rendered at <200.0, 400.0>', 'refresh', 'quit']

        self._given_a_game_with_events(events).run()
        self._assert_observed_screen_updates(expected_updates, self._screen_observer.messages)

    def test_second_tick_leaves_sprite_position_unchanged(self):
        events = [[], [QUIT_EVENT]]
        expected_updates = [
            'Circle with radius 10 rendered at <200.0, 400.0>', 'refresh',
            'Circle with radius 10 rendered at <200.0, 400.0>', 'refresh',
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
            'Circle with radius 10 rendered at <200.0, 400.0>', 'refresh',
            'Circle with radius 10 rendered at <205.0, 400.0>', 'refresh',
            'Circle with radius 10 rendered at <210.0, 400.0>', 'refresh',
            'Circle with radius 10 rendered at <215.0, 400.0>', 'refresh',
            'Circle with radius 10 rendered at <215.0, 400.0>', 'refresh',
            'Circle with radius 10 rendered at <215.0, 400.0>', 'refresh',
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
            'Circle with radius 10 rendered at <200.0, 400.0>', 'refresh',
            'Circle with radius 10 rendered at <195.0, 400.0>', 'refresh',
            'Circle with radius 10 rendered at <190.0, 400.0>', 'refresh',
            'Circle with radius 10 rendered at <185.0, 400.0>', 'refresh',
            'Circle with radius 10 rendered at <185.0, 400.0>', 'refresh',
            'Circle with radius 10 rendered at <185.0, 400.0>', 'refresh',
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
            'Circle with radius 10 rendered at <200.0, 400.0>', 'refresh',
            'Circle with radius 10 rendered at <200.0, 395.0>', 'refresh',
            'Circle with radius 10 rendered at <200.0, 390.0>', 'refresh',
            'Circle with radius 10 rendered at <200.0, 385.0>', 'refresh',
            'Circle with radius 10 rendered at <200.0, 385.0>', 'refresh',
            'Circle with radius 10 rendered at <200.0, 385.0>', 'refresh',
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
            'Circle with radius 10 rendered at <200.0, 400.0>', 'refresh',
            'Circle with radius 10 rendered at <200.0, 405.0>', 'refresh',
            'Circle with radius 10 rendered at <200.0, 410.0>', 'refresh',
            'Circle with radius 10 rendered at <200.0, 415.0>', 'refresh',
            'Circle with radius 10 rendered at <200.0, 415.0>', 'refresh',
            'Circle with radius 10 rendered at <200.0, 415.0>', 'refresh',
            'quit'
        ]
        self._given_a_game_with_events(events).run()
        self._assert_observed_screen_updates(expected_updates, self._screen_observer.messages)
