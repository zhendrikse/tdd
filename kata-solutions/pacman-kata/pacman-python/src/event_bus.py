import pygame

from enum import Enum
from typing import List
from game_event import GameEvent


class PyGameEventBus:

    def get_events(self) -> List[Enum]:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return [GameEvent.QUIT]

        return []
