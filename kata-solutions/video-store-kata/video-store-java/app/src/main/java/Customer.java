package com.cleancode.martinfowler.videostore;

import java.util.ArrayList;
import java.util.List;

public class Customer {
  private final String name;
	private final Rentals rentals = new Rentals();

	public Customer (String name) {
		this.name = name;
	}
	
	public void addRental (Rental rental) {
		rentals.addRental(rental);
	}

  public Rentals getRentals() {
    return rentals;
  }
	
	public String getName () {
		return name;
	}
}