from typing import Protocol

class RawDataReader(Protocol):
    @property
    def ritten(self):
        ...

    @property
    def variables(self):
        ...
