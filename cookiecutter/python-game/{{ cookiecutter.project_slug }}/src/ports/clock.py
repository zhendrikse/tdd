from typing import Protocol


class Clock(Protocol):
    def tick(self, rate: int) -> int:
        ...
