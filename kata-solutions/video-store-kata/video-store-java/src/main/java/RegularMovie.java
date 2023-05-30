package com.cleancode.martinfowler.videostore;

public class RegularMovie extends Movie {
    public RegularMovie(String title) {
        super(title);
    }

    @Override
    public double determineAmount(int daysRented) {
        double rentalAmount = 2;
        if (daysRented > 2)
            rentalAmount += (daysRented - 2) * 1.5;

        return rentalAmount;
    }

    @Override
    public int determineFrequentRenterPoints(int daysRented) {
        return 1;
    }
}