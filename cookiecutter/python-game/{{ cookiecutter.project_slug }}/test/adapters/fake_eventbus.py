from enum import Enum
from typing import List
from ports.eventbus import EventBus
from game_event import GameEvent


class FakeEventBus(EventBus):
    def __init__(self, event_list: List[List[GameEvent]]):
        self._event_list = event_list
        self._get_events_method_called = -1

    def get_events(self) -> List[GameEvent]:
        self._get_events_method_called += 1
        return self._event_list[self._get_events_method_called]
