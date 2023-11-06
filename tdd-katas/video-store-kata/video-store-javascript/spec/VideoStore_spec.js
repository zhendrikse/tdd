const { Customer, statement } = require("../src/VideoStore");

describe("For a customer", function () {
  const newMovies = {
    F001: { title: "The Cell", code: "new" },
    F002: { title: "The Trigger Movie", code: "new" },
  };
  const childrensMovies = {
    F001: { title: "The Trigger Movie", code: "childrens" },
  };
  const regularMovies = {
    F001: { title: "Plan 9 from Outer Space", code: "regular" },
    F002: { title: "8 1/2", code: "regular" },
    F003: { title: "Eraserhead", code: "regular" },
  };

  it("prints a single new release movie statement", function () {
    let rentals = [{ movieID: "F001", days: 3 }];
    let customer = new Customer("Fred", rentals);
    expect(statement(customer, newMovies)).toEqual(
      "Rental Record for Fred\n\tThe Cell\t9\nAmount owed is 9\nYou earned 2 frequent renter points\n"
    );
  });

  it("prints a dual new release movie statement", function () {
    let rentals = [
      { movieID: "F001", days: 3 },
      { movieID: "F002", days: 3 },
    ];
    let customer = new Customer("Fred", rentals);

    expect(statement(customer, newMovies)).toEqual(
      "Rental Record for Fred\n\tThe Cell\t9\n\tThe Trigger Movie\t9\nAmount owed is 18\nYou earned 4 frequent renter points\n"
    );
  });

  it("prints a single childrens movie statement", function () {
    let rentals = [{ movieID: "F001", days: 3 }];
    let customer = new Customer("Fred", rentals);
    expect(statement(customer, childrensMovies)).toEqual(
      "Rental Record for Fred\n\tThe Trigger Movie\t1.5\nAmount owed is 1.5\nYou earned 1 frequent renter points\n"
    );
  });

  it("prints multiple regular movies statement", function () {
    let rentals = [
      { movieID: "F001", days: 1 },
      { movieID: "F002", days: 2 },
      { movieID: "F003", days: 3 },
    ];
    let customer = new Customer("Fred", rentals);
    expect(statement(customer, regularMovies)).toEqual(
      "Rental Record for Fred\n\tPlan 9 from Outer Space\t2\n\t8 1/2\t2\n\tEraserhead\t3.5\nAmount owed is 7.5\nYou earned 3 frequent renter points\n"
    );
  });
});
