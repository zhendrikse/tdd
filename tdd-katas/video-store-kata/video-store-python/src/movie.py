from enum import Enum
from dataclasses import dataclass


class MovieType(Enum):
    CHILDRENS = 2
    REGULAR = 0
    NEW_RELEASE = 1


@dataclass(frozen=False)
class Movie:
    _title: str
    _price_code: MovieType

    def get_price_code(self) -> MovieType:
        return self._price_code

    def set_price_code(self, code: MovieType):
        self._price_code = code

    def get_title(self) -> str:
        return self._title
