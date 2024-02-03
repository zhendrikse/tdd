import pytest
from hamcrest import is_, assert_that, has_length
from game import Game
from game_event import GameEvent

from test.adapters.fake_clock import FakeClock
from test.adapters.fake_eventbus import FakeEventBus
from test.adapters.fake_screen import FakeScreen
from test.screen_observer import FakeScreenObserver


class TestGame:
    _screen_observer = None

    @pytest.fixture(autouse=True)
    def screen_observer(self):
        self._screen_observer = FakeScreenObserver()

    @pytest.fixture
    def given_a_game_with_single_quit_event(self):
        screen = FakeScreen(self._screen_observer)
        event_bus = FakeEventBus([[GameEvent.QUIT]])
        return Game(event_bus, FakeClock(), screen)

    @pytest.fixture
    def given_a_game_with_single_tick_and_single_quit_event(self):
        screen = FakeScreen(self._screen_observer)
        event_bus = FakeEventBus([[], [GameEvent.QUIT]])
        return Game(event_bus, FakeClock(), screen)

    def test_first_tick_draws_sprite_at_50_50(self, given_a_game_with_single_quit_event):
        given_a_game_with_single_quit_event.run()

        assert_that(self._screen_observer.messages, has_length(3))
        assert_that(self._screen_observer.messages[0], is_('Circle with radius 40 rendered at <50.0, 50>'))
        assert_that(self._screen_observer.messages[1], is_('refresh'))
        assert_that(self._screen_observer.messages[2], is_('quit'))

    def test_second_tick_moves_sprite(self, given_a_game_with_single_tick_and_single_quit_event):
        given_a_game_with_single_tick_and_single_quit_event.run()

        assert_that(self._screen_observer.messages, has_length(5))
        assert_that(self._screen_observer.messages[0], is_('Circle with radius 40 rendered at <50.0, 50>'))
        assert_that(self._screen_observer.messages[1], is_('refresh'))
        assert_that(self._screen_observer.messages[2], is_('Circle with radius 40 rendered at <54.8, 50>'))
        assert_that(self._screen_observer.messages[3], is_('refresh'))
        assert_that(self._screen_observer.messages[4], is_('quit'))


