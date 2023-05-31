class Rental:
	def __init__(self, movie, daysRented):
		self._movie 		= movie
		self._daysRented = daysRented
	
	def getDaysRented (self):
		return self._daysRented
	
	def getMovie (self):
		return self._movie
