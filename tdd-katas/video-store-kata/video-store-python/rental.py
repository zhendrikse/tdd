from dataclasses import dataclass

@dataclass(frozen = True)
class Rental:
  _movie: str
  _daysRented: int
	
  def get_days_rented (self):
    return self._daysRented
  
  def get_movie (self):
    return self._movie
