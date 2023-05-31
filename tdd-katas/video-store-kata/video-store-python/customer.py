from movie import MovieType

class Customer:
  def __init__(self, name):
    self._name = name
    self._rentals = []

  def add_rental(self, rental): 
    self._rentals.append (rental)
	
  def get_name (self):
    return self._name
	
  def statement (self):
    totalAmount 			= 0
    frequentRenterPoints 	= 0
    result 					= "Rental Record for " + self.get_name () + "\n"
		
    for rental in self._rentals:
      thisAmount = 0
			
      # determines the amount for each line
      movieType = rental.get_movie ().get_price_code () 
      if movieType == MovieType.REGULAR:
        thisAmount += 2
        if rental.get_days_rented() > 2:
          thisAmount += (rental.get_days_rented() - 2) * 1.5
      elif movieType ==	MovieType.NEW_RELEASE:
        thisAmount += rental.get_days_rented() * 3
      elif movieType == MovieType.CHILDRENS:
        thisAmount += 1.5
        if rental.get_days_rented() > 3:
          thisAmount += (rental.get_days_rented() - 3) * 1.5
			
      frequentRenterPoints += 1
			
      if rental.get_movie ().get_price_code () == MovieType.NEW_RELEASE and rental.get_days_rented() > 1:
        frequentRenterPoints += 1
				
      result += "\t" + rental.get_movie ().get_title () + "\t" + "{:.1f}".format(thisAmount) + "\n"
      totalAmount += thisAmount
		
    result += "You owed " + "{:.1f}".format(totalAmount) + "\n"
    result += "You earned " + str (frequentRenterPoints) + " frequent renter points\n"		
		
    return result
