import pygame

class GameLoop:

    def run(self, game):
        pygame.init()
        screen = pygame.display.set_mode((1280, 720))
        clock = pygame.time.Clock()
        running = True
        dt = 0
        
        while running:
            if game.tick(dt, screen):
                running = False
            pygame.display.flip()
            dt = clock.tick(60)
        
        pygame.quit()
