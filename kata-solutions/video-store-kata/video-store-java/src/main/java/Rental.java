public class Rental {
	private final Movie movie;
	private final int daysRented;

  public Rental (final Movie movie, final int daysRented) {
		this.movie 		= movie;
		this.daysRented = daysRented;
	}
	
	public int getDaysRented () {
		return daysRented;
	}
	
	public Movie getMovie () {
		return movie;
	}

  public int determineFrequentRenterPoints() {
    return movie.determineFrequentRenterPoints(daysRented);
  }

  public double determineAmount() {
    return movie.determineAmount(daysRented);
  }
}