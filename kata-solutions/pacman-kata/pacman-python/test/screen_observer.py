from typing import List

from .observer import Observer


class FakeScreenObserver(Observer):
    def __init__(self):
        self._messages: List[str] = []

    def notify(self, message: str) -> None:
        self._messages.append(message)

    @property
    def messages(self) -> List[str]:
        return self._messages
