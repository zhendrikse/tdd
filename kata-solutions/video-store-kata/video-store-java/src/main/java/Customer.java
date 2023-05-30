package com.cleancode.martinfowler.videostore;

import java.util.ArrayList;
import java.util.List;

public class Customer 
{
	public Customer (String name) {
		this.name = name;
	}
	
	public void addRental (Rental rental) {
		rentals.add (rental);
	}
	
	public String getName () {
		return name;
	}
	
	public String statement () {
		double 				totalAmount 			= 0;
		int					frequentRenterPoints 	= 0;
		String 				result 					= "Rental Record for " + getName () + "\n";
		
		for (Rental rental :rentals) {
			double 		thisAmount = 0;
			
			// determines the amount for each line
			switch (rental.getMovie ().getPriceCode ()) {
				case Movie.REGULAR:
					thisAmount += 2;
					if (rental.getDaysRented () > 2)
						thisAmount += (rental.getDaysRented () - 2) * 1.5;
					break;
				case Movie.NEW_RELEASE:
					thisAmount += rental.getDaysRented () * 3;
					break;
				case Movie.CHILDRENS:
					thisAmount += 1.5;
					if (rental.getDaysRented () > 3)
						thisAmount += (rental.getDaysRented () - 3) * 1.5;
					break;
			}
			
			frequentRenterPoints++;
			
			if (rental.getMovie ().getPriceCode () == Movie.NEW_RELEASE 
					&& rental.getDaysRented () > 1)
				frequentRenterPoints++;
				
			result += "\t" + rental.getMovie ().getTitle () + "\t"
								+ String.valueOf (thisAmount) + "\n";
			totalAmount += thisAmount;
				
		}
		
		result += "You owed " + String.valueOf (totalAmount) + "\n";
		result += "You earned " + String.valueOf (frequentRenterPoints) + " frequent renter points\n";
		
		
		return result;
	}
	

	private String name;
	private List<Rental> rentals = new ArrayList<> ();
}