from src.movie import MovieType

class Customer:
  def __init__(self, name):
    self._name = name
    self._rentals = []

  def add_rental(self, rental): 
    self._rentals.append (rental)
	
  def get_name (self):
    return self._name
	
  def statement (self):
    total_amount 			= 0
    frequent_renter_points 	= 0
    result 					= "Rental Record for " + self.get_name () + "\n"
		
    for rental in self._rentals:
      this_amount = 0
			
      # determines the amount for each line
      movie_type = rental.get_movie ().get_price_code () 
      if movie_type == MovieType.REGULAR:
        this_amount += 2
        if rental.get_days_rented() > 2:
          this_amount += (rental.get_days_rented() - 2) * 1.5
      elif movie_type ==	MovieType.NEW_RELEASE:
        this_amount += rental.get_days_rented() * 3
      elif movie_type == MovieType.CHILDRENS:
        this_amount += 1.5
        if rental.get_days_rented() > 3:
          this_amount += (rental.get_days_rented() - 3) * 1.5
			
      frequent_renter_points += 1
			
      if rental.get_movie ().get_price_code () == MovieType.NEW_RELEASE and rental.get_days_rented() > 1:
        frequent_renter_points += 1
				
      result += "\t" + rental.get_movie ().get_title () + "\t" + "{:.1f}".format(this_amount) + "\n"
      total_amount += this_amount
		
    result += "You owed " + "{:.1f}".format(total_amount) + "\n"
    result += "You earned " + str (frequent_renter_points) + " frequent renter points\n"		
		
    return result
