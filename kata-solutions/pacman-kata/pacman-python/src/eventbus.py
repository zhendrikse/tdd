from enum import Enum
from typing import List, Protocol


class EventBus(Protocol):

    def get_events(self) -> List[Enum]:
        ...
