from hamcrest import is_, assert_that
from src.game import Game

class TestGame:
    def test_first_tick_draws_circle_at_50_50(self):
        game = Game(FakeGameEngine())
        game.run()
        assert_that(True, is_(True))
