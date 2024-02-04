from abc import abstractmethod
from typing import Protocol


class Observer(Protocol):
    @abstractmethod
    def notify(self, message: str) -> None:
        ...
