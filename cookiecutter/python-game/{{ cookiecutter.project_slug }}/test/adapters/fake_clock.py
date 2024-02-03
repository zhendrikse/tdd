from ports.clock import Clock


class FakeClock(Clock):
    def tick(self, rate: int) -> int:
        return 1000 // rate
