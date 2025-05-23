from src.ports.clock import Clock
from src.coordinates import PROXIMITY_TOLERANCE


class FakeClock(Clock):
    def tick(self, rate: float) -> int:
        return (PROXIMITY_TOLERANCE + 1) * 10
