from regular_movie import RegularMovie
from new_release_movie import NewReleaseMovie
from childrens_movie import ChildrensMovie

class Statement:
  def __init__(self, rentals, name):
    self._name = name
    self._rentals = rentals

  def calculate_amount(self):
    return sum(rental.calculate_amount() for rental in self._rentals)

  def calculate_frequent_renter_points(self):
    return sum(rental.calculate_frequent_renter_points() for rental in self._rentals)
    
  def __repr__(self):
    result = "Rental Record for " + self._name + "\n"
    for rental in self._rentals:
      result += "\t" + rental.get_movie ().get_title () + "\t" + "{:.1f}".format(rental.calculate_amount()) + "\n"
		
    result += "You owed " + "{:.1f}".format(self.calculate_amount()) + "\n"
    result += "You earned " + str (self.calculate_frequent_renter_points()) + " frequent renter points\n"		
		
    return result
