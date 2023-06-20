from dataclasses import dataclass
from movie import Movie

@dataclass(frozen = True)
class Rental:
  _movie: Movie
  _days_rented: int
	
  def get_days_rented (self):
    return self._days_rented
  
  def get_movie (self):
    return self._movie
