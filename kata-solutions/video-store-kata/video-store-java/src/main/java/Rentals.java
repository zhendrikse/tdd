package com.cleancode.martinfowler.videostore;

import java.util.ArrayList;
import java.util.List;

public class Rentals {
	private final List<Rental> rentals = new ArrayList<> ();
	
	public void addRental (Rental rental) {
		rentals.add (rental);
	}

  @Override
  public String toString() {
    String result = "";
    
		for (final Rental rental : rentals) {
			result += "\t" + rental.getMovie ().getTitle () + "\t"
								+ String.valueOf (rental.determineAmount()) + "\n";
		}      

    return result;
  }

  public double getTotalPrice() {
    double totalAmount = 0;
    
    for (final Rental rental : rentals) {
			totalAmount += rental.determineAmount();
		}  

    return totalAmount;
  }

  public int getFrequentRenterPoints() {
    int frequentRenterPoints = 0;
    
    for (final Rental rental : rentals) {
			frequentRenterPoints += rental.determineFrequentRenterPoints();
		}  

    return frequentRenterPoints;
  }
}