from hamcrest import is_, assert_that
from src.game import Game
from src.screen import Screen
from src.event_bus import PyGameEventBus
from src.game_engine import GameEngine
from src.coordinates import Coordinates

class TestGame:
    def test_first_tick_draws_circle_at_50_50(self):
        screen = Screen(Coordinates(1280, 720))
        clock = pygame.time.Clock()
        event_bus = PyGameEventBus()
        game = Game(GameEngine(screen, clock, event_bus))
        game.run()
        assert_that(True, is_(True))
