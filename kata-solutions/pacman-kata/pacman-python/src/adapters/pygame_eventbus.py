import pygame

from enum import Enum
from typing import List
from game_event import GameEvent
from ports.eventbus import EventBus


class PyGameEventBus(EventBus):

    def get_events(self) -> List[Enum]:
        for event in pygame.event.get():
            print(f"event={event}")
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    return [GameEvent.ARROW_UP_PRESSED]
                if event.key == pygame.K_DOWN:
                    return [GameEvent.ARROW_DOWN_PRESSED]
                if event.key == pygame.K_LEFT:
                    return [GameEvent.ARROW_LEFT_PRESSED]
                if event.key == pygame.K_RIGHT:
                    return [GameEvent.ARROW_RIGHT_PRESSED]
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    return [GameEvent.ARROW_UP_RELEASED]
                if event.key == pygame.K_DOWN:
                    return [GameEvent.ARROW_DOWN_RELEASED]
                if event.key == pygame.K_LEFT:
                    return [GameEvent.ARROW_LEFT_RELEASED]
                if event.key == pygame.K_RIGHT:
                    return [GameEvent.ARROW_RIGHT_RELEASED]
            if event.type == pygame.QUIT:
                return [GameEvent.QUIT]

        return []
