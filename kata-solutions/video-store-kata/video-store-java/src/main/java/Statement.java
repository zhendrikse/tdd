package com.cleancode.martinfowler.videostore;

import java.util.ArrayList;
import java.util.List;

public class Statement {

    private String customerName;
    private List<Rental> rentals = new ArrayList<>();
    private double totalAmount;
    private int frequentRenterPoints;

    public Statement(String customerName) {
        this.customerName = customerName;
    }

    public void addRental(Rental rental) {
        rentals.add(rental);
    }

    public double getTotal() {
        return totalAmount;
    }

    public int getFrequentRenterPoints() {
        return frequentRenterPoints;
    }

    public String generate() {
        clearTotals();
        String statementText = createHeader();
        statementText += createRentalLines();
        statementText += createFooter();
        return statementText;
    }

    private void clearTotals() {
        totalAmount = 0;
        frequentRenterPoints = 0;
    }

    private String createHeader() {
        return String.format("Rental Record for %s\n", customerName);
    }

    private String createRentalLines() {
        String rentalLinesText = "";
        for (Rental rental : rentals) {
            rentalLinesText += createRentalLine(rental);
        }
        return rentalLinesText;
    }

    private String createRentalLine(Rental rental) {
        double rentalAmount = rental.determineAmount();
        frequentRenterPoints += rental.determineFrequentRenterPoints();
        totalAmount += rentalAmount;

        return formatRentalLine(rental, rentalAmount);
    }

    private String formatRentalLine(Rental rental, double rentalAmount) {
        return String.format("\t%s\t%.1f\n", rental.getTitle(), rentalAmount);
    }

    private String createFooter() {
        return String.format(
                "You owed %.1f\n" +
                        "You earned %d frequent renter points\n",
                totalAmount, frequentRenterPoints);
    }
}