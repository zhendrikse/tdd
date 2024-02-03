from game_event import GameEvent
from typing import List, Protocol


class EventBus(Protocol):

    def get_events(self) -> List[GameEvent]:
        ...
