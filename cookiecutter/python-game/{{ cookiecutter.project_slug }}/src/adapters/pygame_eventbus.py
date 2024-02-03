import pygame

from typing import List
from game_event import GameEvent, KeyPress
from ports.eventbus import EventBus


class PyGameEventBus(EventBus):

    def get_events(self) -> List[GameEvent]:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    return [GameEvent(keypress=KeyPress.ARROW_UP_PRESSED)]
                if event.key == pygame.K_DOWN:
                    return [GameEvent(keypress=KeyPress.ARROW_DOWN_PRESSED)]
                if event.key == pygame.K_LEFT:
                    return [GameEvent(keypress=KeyPress.ARROW_LEFT_PRESSED)]
                if event.key == pygame.K_RIGHT:
                    return [GameEvent(keypress=KeyPress.ARROW_RIGHT_PRESSED)]
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    return [GameEvent(keypress=KeyPress.ARROW_UP_RELEASED)]
                if event.key == pygame.K_DOWN:
                    return [GameEvent(keypress=KeyPress.ARROW_DOWN_RELEASED)]
                if event.key == pygame.K_LEFT:
                    return [GameEvent(keypress=KeyPress.ARROW_LEFT_RELEASED)]
                if event.key == pygame.K_RIGHT:
                    return [GameEvent(keypress=KeyPress.ARROW_RIGHT_RELEASED)]
            elif event.type == pygame.QUIT:
                return [GameEvent(do_quit=True)]

        return []
