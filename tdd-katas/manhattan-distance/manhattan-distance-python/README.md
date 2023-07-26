# Introduction

Please read the general [introduction to the manhattan distance kata](../README.md) first!

# Getting started

First, create an intial Python kata set-up as described [here](https://github.com/zhendrikse/tdd/tree/master/cookiecutter).

Next, go the the newly created project directory and consult
the provided ``README.md`` in there.

# Implementation instructions

We are going to start as simple as possible by defining everything in the specification file and gradually move the code to dedicated classes such `point.py` whenever we deem appropriate.

- Start writing a scenario for a point on a line, i.e. in one dimension, so it only needs one coordinate: 
   1. Let's specify first that the distance to itself is zero.

     a. Let's first write the scenario:
   ```python
   with it("has zero distance to itself"):
      expect(manhattanDistance(point_a, point_a)).to(equal(0))
   ```
     b. Implement the `manhattanDistance()` function in the most stupid way possible, just to make the test pass. For this it is also necessary to add a constructor to the `Point` class, but may still be empty!
     
     c. After the test is green, you may want to refactor the hard-coded return value into the `Point` class.
   
   2. Next, specify the distance to a point on the right of the original point.
   
   3. Make the test green and refactor where necessary. Hint: you _have_ to implement the distance in the `Point` class, as you are _not_ allowed to expose any properties, nor access them from outside the class! Remember one of the goals of the kata is to practice encapsulation.

   4. Specify the distance to a point on the left. This ensures no negative distances can be returned!
   
   5. Make the test green and refactor where necessary.
   
   6. Can you think of more edge cases? Remember that you are not allowed to write tests that are green _without_ requiring a modification to the production code.


 - Start writing a scenario for a point in a plane, i.e. in two dimensions, so it needs two coordinates. Do this in a way that you do _not_ have to modify the scenarios that are already there.
   1. Let's specify first that the distance to a point itself in a plane/two-dimensional space is zero.
   2. Now specify the distance to antoher point.
   3. Make the test green and refactor where necessary.
   4. Do we need any additional scenarios/tests?
   
- The final step is to support points in three dimensions, i.e. 
  with an x-, y- and z-axis. According to [three strikes and you
  refactor](http://wiki.c2.com/?ThreeStrikesAndYouRefactor), we 
  now may as well generalize to _N_ dimensions.

  So let's try to refactor the two concrete integer coordinates we have right now into a more generalized list of (two integer) coordinates using the `*args` packing feature of Python. This list can then readily be generalized to _N_ dimensions.
  
  We are going to refactor our code in the following _small_ steps:
  
  1. Refactor the constructor so that it takes `*args` as argument and assign it to the existing `self.x` and `self.y` cooordinates. 
  Hint: use the following code to assign the second optional coordinate:
    ```python
    self.y = args[1] if len(args) > 1 else 0
    ```
  Verify that everything still works by running your tests!
  2. In the constructor, assign the arguments list _also_ to a (at this point redundant) `self.coordinates` member variable
  Verify that everything still works by running your tests!
  3. Refactor the two-dimensional distance function to use the coordinates member variable:
    ```python
    if len(self.coordinates) > 0:
      distance += abs(other_point.coordinates[0] - self.coordinates[0])
    if len(self.coordinates) > 1:
      distance += abs(other_point.coordinates[1] - self.coordinates[1])
    ```
  Verify that everything still works by running your tests!
  4. Remove the now obsolete member variables `self.x` and `self.y`.
  Verify that everything still works by running your tests!
  5. Convert the above if-statements to a generalized loop.
  Verify that everything still works by running your tests!

# Optional: determine all shortest paths

For those that are up to a more challenging extension: determine all possible shortest paths when the points are two-dimensional (see [this web page](https://www.robertdickau.com/manhattan.html) for a nice graphical representation when the horizontal and vertical distances are equal).   

Let's say two points are _x_ blocks separated horizontally and _y_ blocks vertically. This means that the number of possible routes is defined by the number of ways in which we can distribute the _horizontal steps_ over the _total number of steps_, i.e. _x + y_ choose _x_ (where [_n_ choose _k_](https://programming-idioms.org/idiom/67/binomial-coefficient-n-choose-k/1426/python) is defined as the [binomial coefficient](https://en.wikipedia.org/wiki/Binomial_coefficient)). Obviously we reach the same answer when considering the distribution of _vertical steps_ over the _total number of steps_. 

For example, in [the above mentioned web page](https://www.robertdickau.com/manhattan.html) for two points that are 3 blocks separated in both directions we get 6 choose 3 &rarr; (6 x 5 x 4) / (3 x 2 x 1) = 20. This corresponds with the number of routes drawn on that page. 

The simplest extension would thus be to add an additional function that calculates the total number of shortest paths.

The somewhat more complex extension would be to output all paths explicitly in sequence of steps, where `u` is up, `d` is down, `l` is left, and `r` is right. A typical output for two points separated 3 blocks horizontally and 2 vertically would then look something like

```
llluu
lluul
luull 
uulll
llulu
lullu 
ulllu
lulul 
ullul
ulull  
```

![Manhattan distance](./assets/spoiler.png)
<p align="center" ><b>Figure 2</b>: <i>Continue reading the hint below if you can't find the algorithm to find all possible paths yourself.</i></p>

### Hint

You can use the following Python code as inspiration to find all possible paths:
```
>>> from itertools import product
>>> all_routes = list(product( 'ul', repeat=5))
>>> routes_with_two_ups = list(filter(lambda route: route.count('u') == 2, all_routes))
>>> print(routes_with_two_ups)
[('u', 'u', 'l', 'l', 'l'), ('u', 'l', 'u', 'l', 'l'), ('u', 'l', 'l', 'u', 'l'), ('u', 'l', 'l', 'l', 'u'), ('l', 'u', 'u', 'l', 'l'), ('l', 'u', 'l', 'u', 'l'), ('l', 'u', 'l', 'l', 'u'), ('l', 'l', 'u', 'u', 'l'), ('l', 'l', 'u', 'l', 'u'), ('l', 'l', 'l', 'u', 'u')]
```


# References

- [Manhattan distance kata](https://kata-log.rocks/manhattan-distance-kata), the original, unmodified kata.
- [Python sum function](https://realpython.com/python-sum-function/), if you think for-next loops are old-fashioned and want to implement a more Pythonic solution
- [_n_ choose _k_](https://programming-idioms.org/idiom/67/binomial-coefficient-n-choose-k/1426/python) in Python