from .adapters.pygame_screen import PyGameScreen
from .adapters.pygame_eventbus import PyGameEventBus
from .adapters.pygame_clock import PyGameClock
from .game import Game

if __name__ == "__main__":
    game = Game(PyGameEventBus(), PyGameClock(), PyGameScreen())
    game.run()
