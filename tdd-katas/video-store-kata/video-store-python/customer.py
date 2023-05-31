from movie import MovieType

class Customer:
  def __init__(self, name):
    self._name = name
    self._rentals = []

  def addRental(self, rental): 
    self._rentals.append (rental)
	
  def getName (self):
    return self._name
	
  def statement (self):
    totalAmount 			= 0
    frequentRenterPoints 	= 0
    result 					= "Rental Record for " + self.getName () + "\n"
		
    for rental in self._rentals:
      thisAmount = 0
			
      # determines the amount for each line
      movieType = rental.getMovie ().getPriceCode () 
      if movieType == MovieType.REGULAR:
        thisAmount += 2
        if rental.getDaysRented() > 2:
          thisAmount += (rental.getDaysRented () - 2) * 1.5
      elif movieType ==	MovieType.NEW_RELEASE:
        thisAmount += rental.getDaysRented () * 3
      elif movieType == MovieType.CHILDRENS:
        thisAmount += 1.5
        if rental.getDaysRented () > 3:
          thisAmount += (rental.getDaysRented () - 3) * 1.5
			
      frequentRenterPoints += 1
			
      if rental.getMovie ().getPriceCode () == MovieType.NEW_RELEASE and rental.getDaysRented () > 1:
        frequentRenterPoints += 1
				
      result += "\t" + rental.getMovie ().getTitle () + "\t" + "{:.1f}".format(thisAmount) + "\n"
      totalAmount += thisAmount
		
    result += "You owed " + "{:.1f}".format(totalAmount) + "\n"
    result += "You earned " + str (frequentRenterPoints) + " frequent renter points\n"		
		
    return result
