from abc import abstractmethod
from typing import Protocol


class Clock(Protocol):
    @abstractmethod
    def tick(self, rate: float) -> int:
        ...
