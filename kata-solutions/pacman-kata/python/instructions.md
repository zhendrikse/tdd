# Game development and TDD

## Tackling the main loop

Let's start with the simplest thing that could possibly work, a moving circle. 
The circle constantly moves from left to right.

<details>
  <summary>Rendering a moving circle</summary>

```python
# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

pos_x = 50
dt = 0

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE

    pos_x = pos_x + dt * 0.3 if pos_x <= 500 else 50 

    pygame.draw.circle(screen, "red", (pos_x, 50), 40)
    
    dt = clock.tick(60)  # limits FPS to 60

    # flip() the display to put your work on screen
    pygame.display.flip()

pygame.quit()
```
</details>
