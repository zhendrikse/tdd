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
    return self.as_text()

  def as_html(self):
    result = "<h1>Rental Record for <em>" + self._name + "</em></h1>\n"
    
    result += "<table>\n"
    for rental in self._rentals:
      result += "\t<tr><td>" + rental.get_movie_title() + "</td><td>" + "{:.1f}".format(rental.calculate_amount()) + "</td></tr>\n"
    result += "</table>\n"
    
    result += "<p>You owed <em>" + "{:.1f}".format(self.calculate_amount()) + "</em></p>\n"
    result += "<p>You earned <em>" + str (self.calculate_frequent_renter_points()) + "</em> frequent renter points</p>"
    return result
    
  def as_text(self):
    result = "Rental Record for " + self._name + "\n"
    
    for rental in self._rentals:
      result += "\t" + rental.get_movie_title () + "\t" + "{:.1f}".format(rental.calculate_amount()) + "\n"
		
    result += "You owed " + "{:.1f}".format(self.calculate_amount()) + "\n"
    result += "You earned " + str (self.calculate_frequent_renter_points()) + " frequent renter points\n"		
		
    return result
