import pygame
from enum import Enum
from game_event import GameEvent
from typing import List
from coordinates import Coordinates
from eventbus import EventBus
from clock import Clock

class GameEngine:
    def __init__(self, screen, clock: Clock, eventbus: EventBus):
        self._screen = screen
        self._clock = clock
        self._eventbus = eventbus

    def tick(self, rate: int) -> int:
        return self._clock.tick(rate)

    def quit(self):
        self._screen.quit()

    def draw_circle(self, color: str, coordinates: Coordinates, radius: int) -> None:
        self._screen.render_circle(color, coordinates, radius)

    def refresh(self) -> None:
        self._screen.flip()
        self._screen.fill("purple")

    def get_events(self) -> List[Enum]:
        return self._eventbus.get_events()
