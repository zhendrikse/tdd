package com.cleancode.martinfowler.videostore;

import java.util.List;

public class Statement {
  private final Customer customer;

  public Statement (final Customer aCustomer) {
		this.customer = aCustomer;
  }

  public int getFrequentRenterPoints() {
    return customer.getRentals().getFrequentRenterPoints();
  }

  public String getTotalAmountOwedAsString() {
    return String.valueOf (customer.getRentals().getTotalPrice());
  }

  @Override
  public String toString() {
    String statementAsString = "Rental Record for " + customer.getName()  + "\n";
    statementAsString += customer.getRentals().toString();
    statementAsString += "You owed " + getTotalAmountOwedAsString() + "\n";
		statementAsString += "You earned " + getFrequentRenterPoints() + " frequent renter points\n";
    
    return statementAsString;
  }
}