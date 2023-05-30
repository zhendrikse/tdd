package com.cleancode.martinfowler.videostore;

public class NewReleaseMovie extends Movie {
  public NewReleaseMovie(String title) {
    super(title);
  }

  @Override
  public double determineAmount(int daysRented) {
    return daysRented * 3.0;
  }

  @Override
  public int determineFrequentRenterPoints(int daysRented) {
    return (daysRented > 1) ? 2 : 1;
  }
}