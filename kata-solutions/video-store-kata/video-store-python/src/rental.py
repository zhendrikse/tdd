from dataclasses import dataclass
import movie


@dataclass(frozen=True)
class Rental:
    _movie: movie.Movie
    _days_rented: int

    def get_movie_title(self):
        return self._movie.get_title()

    def calculate_amount(self):
        return self._movie.calculate_amount(self._days_rented)

    def calculate_frequent_renter_points(self):
        return self._movie.calculate_frequent_renter_points(self._days_rented)
