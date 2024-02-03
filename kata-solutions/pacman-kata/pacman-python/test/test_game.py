import pytest
from hamcrest import is_, assert_that, has_length
from game import Game
from game_event import GameEvent, KeyPress

from test.adapters.fake_clock import FakeClock
from test.adapters.fake_eventbus import FakeEventBus
from test.adapters.fake_screen import FakeScreen
from test.screen_observer import FakeScreenObserver

QUIT_EVENT = GameEvent(do_quit=True)

class TestGame:
    _screen_observer = None

    @pytest.fixture(autouse=True)
    def screen_observer(self):
        self._screen_observer = FakeScreenObserver()

    @pytest.fixture
    def given_a_game_without_events(self):
        screen = FakeScreen(self._screen_observer)
        event_bus = FakeEventBus([[QUIT_EVENT]])
        return Game(event_bus, FakeClock(), screen)

    @pytest.fixture
    def given_a_game_with_single_empty_tick(self):
        screen = FakeScreen(self._screen_observer)
        event_bus = FakeEventBus([[], [QUIT_EVENT]])
        return Game(event_bus, FakeClock(), screen)

    @pytest.fixture
    def given_a_game_with_right_arrow_pressed_for_some_time(self):
        screen = FakeScreen(self._screen_observer)
        event_bus = FakeEventBus([
                [GameEvent(keypress=KeyPress.ARROW_RIGHT_PRESSED)],
                [],
                [],
                [GameEvent(keypress=KeyPress.ARROW_RIGHT_RELEASED)],
                [],
                [QUIT_EVENT]])
        return Game(event_bus, FakeClock(), screen)

    @pytest.fixture
    def given_a_game_with_left_arrow_pressed_for_some_time(self):
        screen = FakeScreen(self._screen_observer)
        event_bus = FakeEventBus([
                [GameEvent(keypress=KeyPress.ARROW_LEFT_PRESSED)],
                [],
                [],
                [GameEvent(keypress=KeyPress.ARROW_RIGHT_RELEASED)],
                [],
                [QUIT_EVENT]])
        return Game(event_bus, FakeClock(), screen)

    def test_game_without_events_draws_sprite(self, given_a_game_without_events):
        given_a_game_without_events.run()

        assert_that(self._screen_observer.messages, has_length(3))
        assert_that(self._screen_observer.messages[0], is_('Circle with radius 10 rendered at <50, 50>'))
        assert_that(self._screen_observer.messages[1], is_('refresh'))
        assert_that(self._screen_observer.messages[2], is_('quit'))

    def test_second_tick_leaves_sprite_position_unchanged(self, given_a_game_with_single_empty_tick):
        given_a_game_with_single_empty_tick.run()

        assert_that(self._screen_observer.messages, has_length(5))
        assert_that(self._screen_observer.messages[0], is_('Circle with radius 10 rendered at <50, 50>'))
        assert_that(self._screen_observer.messages[1], is_('refresh'))
        assert_that(self._screen_observer.messages[2], is_('Circle with radius 10 rendered at <50, 50>'))
        assert_that(self._screen_observer.messages[3], is_('refresh'))
        assert_that(self._screen_observer.messages[4], is_('quit'))

    def test_move_sprite_to_the_right(self, given_a_game_with_right_arrow_pressed_for_some_time):
        given_a_game_with_right_arrow_pressed_for_some_time.run()

        assert_that(self._screen_observer.messages, has_length(13))
        assert_that(self._screen_observer.messages[0], is_('Circle with radius 10 rendered at <50, 50>'))
        assert_that(self._screen_observer.messages[1], is_('refresh'))
        assert_that(self._screen_observer.messages[2], is_('Circle with radius 10 rendered at <51, 50>'))
        assert_that(self._screen_observer.messages[3], is_('refresh'))
        assert_that(self._screen_observer.messages[4], is_('Circle with radius 10 rendered at <52, 50>'))
        assert_that(self._screen_observer.messages[5], is_('refresh'))
        assert_that(self._screen_observer.messages[6], is_('Circle with radius 10 rendered at <53, 50>'))
        assert_that(self._screen_observer.messages[7], is_('refresh'))
        assert_that(self._screen_observer.messages[8], is_('Circle with radius 10 rendered at <53, 50>'))
        assert_that(self._screen_observer.messages[9], is_('refresh'))
        assert_that(self._screen_observer.messages[10], is_('Circle with radius 10 rendered at <53, 50>'))
        assert_that(self._screen_observer.messages[11], is_('refresh'))
        assert_that(self._screen_observer.messages[12], is_('quit'))

    def test_move_sprite_to_the_left(self, given_a_game_with_left_arrow_pressed_for_some_time):
        given_a_game_with_left_arrow_pressed_for_some_time.run()

        assert_that(self._screen_observer.messages, has_length(13))
        assert_that(self._screen_observer.messages[0], is_('Circle with radius 10 rendered at <50, 50>'))
        assert_that(self._screen_observer.messages[1], is_('refresh'))
        assert_that(self._screen_observer.messages[2], is_('Circle with radius 10 rendered at <49, 50>'))
        assert_that(self._screen_observer.messages[3], is_('refresh'))
        assert_that(self._screen_observer.messages[4], is_('Circle with radius 10 rendered at <48, 50>'))
        assert_that(self._screen_observer.messages[5], is_('refresh'))
        assert_that(self._screen_observer.messages[6], is_('Circle with radius 10 rendered at <47, 50>'))
        assert_that(self._screen_observer.messages[7], is_('refresh'))
        assert_that(self._screen_observer.messages[8], is_('Circle with radius 10 rendered at <47, 50>'))
        assert_that(self._screen_observer.messages[9], is_('refresh'))
        assert_that(self._screen_observer.messages[10], is_('Circle with radius 10 rendered at <47, 50>'))
        assert_that(self._screen_observer.messages[11], is_('refresh'))
        assert_that(self._screen_observer.messages[12], is_('quit'))



