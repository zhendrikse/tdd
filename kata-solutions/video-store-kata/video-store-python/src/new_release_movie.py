from movie import Movie

class NewReleaseMovie(Movie):
  def __init__(self, title):
    super().__init__(title)

  def calculate_amount(self, days_rented):
    return days_rented * 3

  def calculate_frequent_renter_points(self, days_rented):
    if days_rented > 1:
        return 2
    return 1
