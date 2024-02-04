from abc import abstractmethod
from ..game_event import GameEvent
from typing import List, Protocol


class EventBus(Protocol):

    @abstractmethod
    def get_events(self) -> List[GameEvent]:
        ...
