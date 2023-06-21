# Possible approach

## Step 1: [extract class](https://refactoring.guru/extract-class)

Let's first address the [large class](https://refactoring.guru/smells/large-class)
code smell in the `customer.py` by creating a `statement.py`

```python
class Statement:
  def __init__(self, rentals, name):
    self.total_amount 			= 0
    self.frequent_renter_points 	= 0
    self.result 					= "Rental Record for " + name + "\n"
    self._rentals = rentals

  def __repr__(self):
    for rental in self._rentals:
      this_amount = 0
			
      # determines the amount for each line
      movie_type = rental.get_movie ().get_price_code () 
      if movie_type == MovieType.REGULAR:
        this_amount += 2
        if rental.get_days_rented() > 2:
          this_amount += (rental.get_days_rented() - 2) * 1.5
      elif movie_type ==	MovieType.NEW_RELEASE:
        this_amount += rental.get_days_rented() * 3
      elif movie_type == MovieType.CHILDRENS:
        this_amount += 1.5
        if rental.get_days_rented() > 3:
          this_amount += (rental.get_days_rented() - 3) * 1.5
			
      self.frequent_renter_points += 1
			
      if rental.get_movie ().get_price_code () == MovieType.NEW_RELEASE and rental.get_days_rented() > 1:
        self.frequent_renter_points += 1
				
      self.result += "\t" + rental.get_movie ().get_title () + "\t" + "{:.1f}".format(this_amount) + "\n"
      self.total_amount += this_amount
		
    self.result += "You owed " + "{:.1f}".format(self.total_amount) + "\n"
    self.result += "You earned " + str (self.frequent_renter_points) + " frequent renter points\n"		
		
    return self.result
```

with which the `Customer` simplifies to

```python
class Customer:
  # ...
  	
  def statement (self):
    return str(Statement(self._rentals, self._name))
```

Moreover, we can reduce the scope of the `total_amount` and `frequent_renter_points`
variables by moving then inside the `__repr__()` method like so

```python
  def __repr__(self):
    total_amount 			= 0
    frequent_renter_points 	= 0
    for rental in self._rentals:
      # ...
```

Finally, the `get_name()` method in `Customer` can and hence should be removed.

## Step 2: [replace conditional with polymorphism](https://refactoring.guru/replace-conditional-with-polymorphism)

Let's first extract the calculation of the amount due in a separate method
by using [extract method](https://refactoring.guru/extract-method)

```python
    
  def calculate_amount(self, rental):
    amount = 2
    if rental.get_days_rented() > 2:
      amount += (rental.get_days_rented() - 2) * 1.5
    return amount 

  def __repr__(self):
			# ...
    
      # determines the amount for each line
      movie_type = rental.get_movie ().get_price_code () 
      if movie_type == MovieType.REGULAR:
        this_amount += self.calculate_amount(rental)
```

As this calculation is specific to a regular movie, let's put that logic
into a dedicated `RegularMovie` class

```python
class RegularMovie:
  def calculate_amount(self, days_rented):
    amount = 2
    if days_rented > 2:
      amount += (days_rented - 2) * 1.5
    return amount 
```

which leads to

```python
			# ...
    			
      # determines the amount for each line
      movie_type = rental.get_movie ().get_price_code () 
      if movie_type == MovieType.REGULAR:
        this_amount += RegularMovie().calculate_amount(rental.get_days_rented())
```

We can do _mutatis mutandum_ the same for the other movie types.

```python
      # determines the amount for each line
      movie_type = rental.get_movie ().get_price_code () 
      if movie_type == MovieType.REGULAR:
        this_amount += RegularMovie().calculate_amount(rental.get_days_rented())
      elif movie_type ==	MovieType.NEW_RELEASE:
        this_amount += NewReleaseMovie().calculate_amount(rental.get_days_rented())
      elif movie_type == MovieType.CHILDRENS:
        this_amount += ChildrensMovie().calculate_amount(rental.get_days_rented())
```

Let's do the same with the calculation of the frequent renter points:

```python
      # determines the amount for each line
      movie_type = rental.get_movie ().get_price_code () 
      if movie_type == MovieType.REGULAR:
        this_amount += RegularMovie().calculate_amount(rental.get_days_rented())
        frequent_renter_points += RegularMovie().calculate_frequent_renter_points(rental.get_days_rented())
      elif movie_type ==	MovieType.NEW_RELEASE:
        this_amount += NewReleaseMovie().calculate_amount(rental.get_days_rented())
        frequent_renter_points += NewReleaseMovie().calculate_frequent_renter_points(rental.get_days_rented())
      elif movie_type == MovieType.CHILDRENS:
        this_amount += ChildrensMovie().calculate_amount(rental.get_days_rented())
        frequent_renter_points += ChildrensMovie().calculate_frequent_renter_points(rental.get_days_rented())
```

which can then be simplified to

```python
      # determines the amount for each line
      movie_type = rental.get_movie ().get_price_code ()
      movie = None
      if movie_type == MovieType.REGULAR:
        movie = RegularMovie()
      elif movie_type ==	MovieType.NEW_RELEASE:
        movie = NewReleaseMovie()
      elif movie_type == MovieType.CHILDRENS:
        movie = ChildrensMovie()

      this_amount += movie.calculate_amount(rental.get_days_rented())
      frequent_renter_points += movie.calculate_frequent_renter_points(rental.get_days_rented())
```
Let's now make our first move towards polymorphism by making the movie
subclasses inherit from the `Movie` base class

```python
from movie import Movie, MovieType

class RegularMovie(Movie):
  def __init__(self, title = ""):
    super().__init__(title, MovieType.REGULAR)
```

and analogously for the other movie sub-types. This allows us to modify the
creation of rentals in the test class one by one like so

```python
from new_release_movie import NewReleaseMovie

@pytest.fixture
def customer():
  return  Customer("Fred")

def testSingleNewReleaseStatement(customer):
    customer.add_rental(Rental(NewReleaseMovie("The Cell"), 3))
    assert "Rental Record for Fred\n\tThe Cell\t9.0\nYou owed 9.0\nYou earned 2 frequent renter points\n" == customer.statement()
```

Now that we are creating the right movie types in the tests, we can get
rid of the `if`-statements in the `Statement` class

```python
    for rental in self._rentals:
      this_amount = 0
      movie = rental.get_movie ()
      this_amount += movie.calculate_amount(rental.get_days_rented())
      frequent_renter_points += movie.calculate_frequent_renter_points(rental.get_days_rented())

      # ...
```

Finally, we can get rid of the `MovieType` s altogether: we clean up the
`Movie` class by removing the `price_code` and modifying the subclasses
accordingly 

```python
from movie import Movie

class ChildrensMovie(Movie):
  def __init__(self, title):
    super().__init__(title)
```

Note that we also removed the possibility of a 
default empty `title` parameter in the constructor. It isn't 
necessary anymore and shouldn't be allowed for anyways.

## Step 3: [inappropriate intimacy](https://refactoring.guru/smells/inappropriate-intimacy)

We observe that the `Statement` and `Rental` classes exhibit an [inappropriate intimacy](https://refactoring.guru/smells/inappropriate-intimacy). 
Let's refactor the calculation of both the frequent renter points as
well as the amount due in the `Rental` class itself.

```python
class Rental:
  # ...
  
  def calculate_amount(self):
    return self._movie.calculate_amount(self._days_rented)

  def calculate_frequent_renter_points(self):
    return self._movie.calculate_frequent_renter_points(self._days_rented)
```

with which the `Statement` class becomes

```python
    for rental in self._rentals:
      this_amount = rental.calculate_amount()
      frequent_renter_points += rental.calculate_frequent_renter_points()
```

This in turn implies that we can/should remove the `get_days_rented (self)` method
from the `Rental` class.

## Step 4: [extract method](https://refactoring.guru/extract-method)

We can apply the [extract method](https://refactoring.guru/extract-method)
refactoring twice to further clean up the `Statement` class:

```python
class Statement:
  def __init__(self, rentals, name):
    self._name = name
    self._rentals = rentals

  def calculate_amount(self):
    return sum(rental.calculate_amount() for rental in self._rentals)

  def calculate_frequent_renter_points(self):
    return sum(rental.calculate_frequent_renter_points() for rental in self._rentals)
    
  def __repr__(self):
    result = "Rental Record for " + self._name + "\n"
    for rental in self._rentals:
      result += "\t" + rental.get_movie ().get_title () + "\t" + "{:.1f}".format(rental.calculate_amount()) + "\n"
		
    result += "You owed " + "{:.1f}".format(self.calculate_amount()) + "\n"
    result += "You earned " + str (self.calculate_frequent_renter_points()) + " frequent renter points\n"		
		
    return result
``` 

This also allows us to test more specifically on the expected amounts due
and frequent renter points. To this extent, we let the `Customer` return
the `Statement` instead of a string, and make the conversion to 
string happen in the test class itself.

```python
def testSingleNewReleaseStatement(customer):
    customer.add_rental(Rental(NewReleaseMovie("The Cell"), 3))
    assert "Rental Record for Fred\n\tThe Cell\t9.0\nYou owed 9.0\nYou earned 2 frequent renter points\n" == str(customer.statement())
    assert 2 == customer.statement().calculate_frequent_renter_points()
    assert 9.0 == customer.statement().calculate_amount()
```

Now we can/should apply the [single assert per test](https://www.qwan.eu/2021/08/27/tdd-one-assert-per-test.html) heuristic:

```python
class TestSingleNewReleaseRental:
  @pytest.fixture(autouse = True)
  def customer(self):
      self._customer = Customer("Fred")
      self._customer.add_rental(Rental(NewReleaseMovie("The Cell"), 3))
  
  def test_statement_as_test(self):
      assert "Rental Record for Fred\n\tThe Cell\t9.0\nYou owed 9.0\nYou earned 2 frequent renter points\n" == str(self._customer.statement())

  def test_frequent_renter_points(self):
      assert 2 == self._customer.statement().calculate_frequent_renter_points()

  def test_total_amount(self):
      assert 9.0 == self._customer.statement().calculate_amount()
```

## Step 5: preparations for the HTML extension

As we eventually want to create an additional HTML rendering of 
the rental statement, it makes sense to first transform the 
`get_movie()` method in the `Rental` class to `get_movie_title()`

```python
  def get_movie_title(self):
    return self._movie.get_title()
```

as this both improves encapsulation as well as simplifies the 
call to it from within the `Statement` class.

Let's create an `as_text()` method in preparation of the newly required
`as_html()` method.

```python
  def __repr__(self):
    return self.as_text()
    
  def as_text(self):
    result = "Rental Record for " + self._name + "\n"
    for rental in self._rentals:
      result += "\t" + rental.get_movie_title () + "\t" + "{:.1f}".format(rental.calculate_amount()) + "\n"
		
    result += "You owed " + "{:.1f}".format(self.calculate_amount()) + "\n"
    result += "You earned " + str (self.calculate_frequent_renter_points()) + " frequent renter points\n"		
		
    return result
```

Now it is time to create an HTML version of the text-based rental statement

```
Rental Record for Fred
  The Cell  9.0
  The Tigger Movie  9.0
You owed 18.0
You earned 4 frequent renter points
```
&rarr;

```html
<h1>Rental Record for <em>Fred</em></h1>
<table>
  <tr><td>The Cell</td><td>9.0</td></tr>
  <tr><td>The Tigger Movie</td><td>9.0</td></tr>
</table>
<p>You owed <em>18.0</em></p>
<p>You earned <em>4</em> frequent renter points</p>
```

So let's create a test first!

```python  
  def test_statement_as_html(self):
      assert "<h1>Rental Record for <em>Fred</em></h1>\n<table>\n\t<tr><td>The Cell</td><td>9.0</td></tr>\n\t<tr><td>The Tigger Movie</td><td>9.0</td></tr>\n</table>\n<p>You owed <em>18.0</em></p>\n<p>You earned <em>4</em> frequent renter points</p>" == self._customer.statement().as_html()
```

and define the `as_html()` accordingly

```python

  def as_html(self):
    return "<h1>Rental Record for <em>Fred</em></h1>\n<table>\n\t<tr><td>The Cell</td><td>9.0</td></tr>\n\t<tr><td>The Tigger Movie</td><td>9.0</td></tr>\n</table>\n<p>You owed <em>18.0</em></p>\n<p>You earned <em>4</em> frequent renter points</p>"
```

Now we immediately observe duplication in the test and production code,
so let's generalize this.

```python
  def as_html(self):
    result = "<h1>Rental Record for <em>" + self._name + "</em></h1>\n"
    
    result += "<table>\n"
    for rental in self._rentals:
      result += "\t<tr><td>" + rental.get_movie_title() + "</td><td>" + "{:.1f}".format(rental.calculate_amount()) + "</td></tr>\n"
    result += "</table>\n"
    
    result += "<p>You owed <em>" + "{:.1f}".format(self.calculate_amount()) + "</em></p>\n"
    result += "<p>You earned <em>" + str (self.calculate_frequent_renter_points()) + "</em> frequent renter points</p>"
    return result
  ```

  Now note the similarity between the `as_html()` and `as_text()` methods! 