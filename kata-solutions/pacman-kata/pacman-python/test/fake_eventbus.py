from enum import Enum
from typing import List


class FakeEventBus:
    def __init__(self, event_list: List[List[Enum]]):
        self._event_list = event_list
        self._get_events_method_called = -1

    def get_events(self) -> List[Enum]:
        self._get_events_method_called += 1
        return self._event_list[self._get_events_method_called]
