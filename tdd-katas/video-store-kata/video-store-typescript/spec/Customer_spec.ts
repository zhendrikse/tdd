"use strict";

import { expect } from "chai";
import { Customer, Rental, Movie, MovieType } from "../src/Customer";

describe("For a customer with rentals", function () {
  let customer: Customer;

  beforeEach(() => {
    customer = new Customer("Fred");
  });

  it("prints a single new release statement", () => {
    customer.addRental(
      new Rental(new Movie("The Cell", MovieType.NEW_RELEASE), 3)
    );
    expect(customer.statement()).to.equal(
      "Rental Record for Fred\n\tThe Cell\t9\nAmount owed is 9\nYou earned 2 frequent renter points\n"
    );
  });

  it("prints a dual new release statement", () => {
    customer.addRental(
      new Rental(new Movie("The Cell", MovieType.NEW_RELEASE), 3)
    );
    customer.addRental(
      new Rental(new Movie("The Tigger Movie", MovieType.NEW_RELEASE), 3)
    );
    expect(customer.statement()).to.equal(
      "Rental Record for Fred\n\tThe Cell\t9\n\tThe Tigger Movie\t9\nAmount owed is 18\nYou earned 4 frequent renter points\n"
    );
  });

  it("prints a single childrens movie statement", () => {
    customer.addRental(
      new Rental(new Movie("The Tigger Movie", MovieType.CHILDRENS), 3)
    );
    expect(customer.statement()).to.equal(
      "Rental Record for Fred\n\tThe Tigger Movie\t1.5\nAmount owed is 1.5\nYou earned 1 frequent renter points\n"
    );
  });

  it("prints multiple regular movies statement", () => {
    customer.addRental(
      new Rental(new Movie("Plan 9 from Outer Space", MovieType.REGULAR), 1)
    );
    customer.addRental(new Rental(new Movie("8 1/2", MovieType.REGULAR), 2));
    customer.addRental(
      new Rental(new Movie("Eraserhead", MovieType.REGULAR), 3)
    );

    expect(customer.statement()).to.equal(
      "Rental Record for Fred\n\tPlan 9 from Outer Space\t2\n\t8 1/2\t2\n\tEraserhead\t3.5\nAmount owed is 7.5\nYou earned 3 frequent renter points\n"
    );
  });
});
