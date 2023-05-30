package com.cleancode.martinfowler.videostore;

public class Movie {
	
	private String title;
	private int priceCode;
	
	public Movie (String title) {
		this.title 		= title;
	}
	
	
	public String getTitle () {
		return title;
	}

  public double determineAmount(int daysRented) {
    return 0;
  }
  
  public int determineFrequentRenterPoints(int daysRented) {
    return 1;
  }

}