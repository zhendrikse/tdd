from enum import Enum
from typing import List

from src.game_event import GameEvent


class FakeEventBus:
    def get_events(self) -> List[Enum]:
        return [GameEvent.QUIT]
