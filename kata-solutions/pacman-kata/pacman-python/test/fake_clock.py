class FakeClock:
    def tick(self, rate: int) -> int:
        return 1000 // rate
