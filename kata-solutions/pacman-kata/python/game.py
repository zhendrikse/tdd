import pygame
from game_loop import GameLoop

class Game:

    def __init__(self, game_loop):
        self._game_loop = game_loop
        self._x = 50

    def run(self):
        self._game_loop.run(self)

    def tick(self, dt, screen) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        
        self._x = self._x + dt * 0.3 if self._x <=500 else 50
        
        screen.fill("purple")
        pygame.draw.circle(screen, "red", (self._x, 50), 40)

if __name__ == "__main__":
   Game(GameLoop()).run()
