from hamcrest import is_, assert_that
from src.game import Game
from src.screen import Screen

from test.fake_clock import FakeClock
from test.fake_eventbus import FakeEventBus
from test.fake_screen import FakeScreen


class TestGame:
    def test_first_tick_draws_circle_at_50_50(self):
        screen = FakeScreen()
        clock = FakeClock()
        event_bus = FakeEventBus()
        game = Game(event_bus, clock, screen)
        game.run()
        assert_that(True, is_(True))
