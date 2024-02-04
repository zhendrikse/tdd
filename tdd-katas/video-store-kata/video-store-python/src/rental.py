from dataclasses import dataclass
from .movie import Movie


@dataclass(frozen=True)
class Rental:
    _movie: Movie
    _days_rented: int

    def get_days_rented(self) -> int:
        return self._days_rented

    def get_movie(self) -> Movie:
        return self._movie
