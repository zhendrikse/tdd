import pytest
from customer import Customer
from rental import Rental
from movie  import Movie, MovieType

def testSingleNewReleaseStatement():
    customer = Customer("Fred")
    customer.add_rental(Rental(Movie("The Cell", MovieType.NEW_RELEASE), 3))
    assert "Rental Record for Fred\n\tThe Cell\t9.0\nYou owed 9.0\nYou earned 2 frequent renter points\n" == customer.statement()

def test_DualNewReleaseStatement():
    customer = Customer("Fred")
    customer.add_rental(Rental(Movie("The Cell", MovieType.NEW_RELEASE), 3))
    customer.add_rental(Rental(Movie("The Tigger Movie", MovieType.NEW_RELEASE), 3))
    assert "Rental Record for Fred\n\tThe Cell\t9.0\n\tThe Tigger Movie\t9.0\nYou owed 18.0\nYou earned 4 frequent renter points\n" == customer.statement()
  
def test_SingleChildrensStatement():
    customer = Customer("Fred")
    customer.add_rental(Rental(Movie("The Tigger Movie", MovieType.CHILDRENS), 3))
    assert "Rental Record for Fred\n\tThe Tigger Movie\t1.5\nYou owed 1.5\nYou earned 1 frequent renter points\n" == customer.statement()

def test_MultipleRegularStatement():
    customer = Customer("Fred")
    customer.add_rental(Rental(Movie("Plan 9 from Outer Space", MovieType.REGULAR), 1))
    customer.add_rental(Rental(Movie("8 1/2", MovieType.REGULAR), 2))
    customer.add_rental(Rental(Movie("Eraserhead", MovieType.REGULAR), 3))

    assert "Rental Record for Fred\n\tPlan 9 from Outer Space\t2.0\n\t8 1/2\t2.0\n\tEraserhead\t3.5\nYou owed 7.5\nYou earned 3 frequent renter points\n" == customer.statement()
