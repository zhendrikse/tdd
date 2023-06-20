from dataclasses import dataclass
from movie import Movie

@dataclass(frozen = True)
class Rental:
  _movie: Movie
  _days_rented: int
  
  def get_movie (self):
    return self._movie

  def calculate_amount(self):
    return self._movie.calculate_amount(self._days_rented)

  def calculate_frequent_renter_points(self):
    return self._movie.calculate_frequent_renter_points(self._days_rented)

  