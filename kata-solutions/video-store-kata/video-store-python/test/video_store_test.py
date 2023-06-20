import pytest
from customer import Customer
from rental import Rental
from new_release_movie import NewReleaseMovie
from childrens_movie import ChildrensMovie
from regular_movie import RegularMovie

class TestSingleNewReleaseRental:
  @pytest.fixture(autouse = True)
  def customer(self):
      self._customer = Customer("Fred")
      self._customer.add_rental(Rental(NewReleaseMovie("The Cell"), 3))
  
  def test_statement(self):
      assert "Rental Record for Fred\n\tThe Cell\t9.0\nYou owed 9.0\nYou earned 2 frequent renter points\n" == str(self._customer.statement())

  def test_frequent_renter_points(self):
      assert 2 == self._customer.statement().calculate_frequent_renter_points()

  def test_total_amount(self):
      assert 9.0 == self._customer.statement().calculate_amount()

class TestDualNewReleaseRental:
  @pytest.fixture(autouse = True)
  def customer(self):
      self._customer = Customer("Fred")
      self._customer.add_rental(Rental(NewReleaseMovie("The Cell"), 3))
      self._customer.add_rental(Rental(NewReleaseMovie("The Tigger Movie"), 3))
    
  def test_DualNewReleaseStatement(self):
      assert "Rental Record for Fred\n\tThe Cell\t9.0\n\tThe Tigger Movie\t9.0\nYou owed 18.0\nYou earned 4 frequent renter points\n" == str(self._customer.statement())

  def test_frequent_renter_points(self):
      assert 4 == self._customer.statement().calculate_frequent_renter_points()

  def test_total_amount(self):
      assert 18 == self._customer.statement().calculate_amount()

class TestSingleChildrensRental:
  @pytest.fixture(autouse = True)
  def customer(self):
      self._customer = Customer("Fred")
      self._customer.add_rental(Rental(ChildrensMovie("The Tigger Movie"), 3))
    
  def test_SingleChildrensStatement(self):
      assert "Rental Record for Fred\n\tThe Tigger Movie\t1.5\nYou owed 1.5\nYou earned 1 frequent renter points\n" == str(self._customer.statement())

  def test_frequent_renter_points(self):
      assert 1 == self._customer.statement().calculate_frequent_renter_points()

  def test_total_amount(self):
      assert 1.5 == self._customer.statement().calculate_amount()

class TestMultipleRegularRental:
  @pytest.fixture(autouse = True)
  def customer(self):
      self._customer = Customer("Fred")
      self._customer.add_rental(Rental(RegularMovie("Plan 9 from Outer Space"), 1))
      self._customer.add_rental(Rental(RegularMovie("8 1/2"), 2))
      self._customer.add_rental(Rental(RegularMovie("Eraserhead"), 3))
  
  def test_MultipleRegularStatement(self):
      assert "Rental Record for Fred\n\tPlan 9 from Outer Space\t2.0\n\t8 1/2\t2.0\n\tEraserhead\t3.5\nYou owed 7.5\nYou earned 3 frequent renter points\n" == str(self._customer.statement())

  def test_frequent_renter_points(self):
      assert 3 == self._customer.statement().calculate_frequent_renter_points()

  def test_total_amount(self):
      assert 7.5 == self._customer.statement().calculate_amount()
