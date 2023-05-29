# [Mars rover kata](https://kata-log.rocks/mars-rover-kata)

![Mars rover](assets/mars-rover.jpg)

The kata can be found [here](https://kata-log.rocks/mars-rover-kata).

## TODO list

- [ ] Directionless rover at the origin
- [ ] Moves forward to north by default
- [ ] Moves backward to south by default
- [ ] Must be able to turn left
- [ ] Must be able to turn right

## Constraints
- Encapsulation (direction should not be exposed)
- Command pattern

# Possible solution 

## A new rover

1. Let's start by default with a directionless rover sitting at the origin
   ```python
   with description(Rover) as self:
     with it("starts at position (0, 0)"):
       self.rover = Rover()
       expect(self.rover.is_at()).to(equal([0, 0]))
   ```
   Implement it hard-coded. After the test passes, introduce an
   immutable ``Coordinate`` data class (using the Python language construct ``@dataclass(frozen = True)``)
   to get rid of the [primitive obsession](https://refactoring.guru/smells/primitive-obsession) code smell.

2. It should move forward north by default
   ```python
   with it("moves forward to the north"):
     self.rover = Rover()
     self.rover.move_forward()
     expect(self.rover.is_at()).to(equal(Coordinates(0, 1)))
   ```
   Apply the DRY principle to the test code.

3. It should move backward south by default
   ```python
   with it("moves backward to the south"):
     self.rover.move_backward()
     expect(self.rover.is_at()).to(equal(Coordinates(0, -1)))
   ```

   Note that we can generalize the hard-coded ``Coordinates(0, 1)`` by noticing that
   it is an ``[0 1]`` increment to the previous coordinates value in the rover. So let's
   add an ``add(self, step)`` to the ``Coordinates`` data class to return incremented
   coordinates like so

   ```python
    def add(self, step):
      return Coordinates(self.x + step.x, self.y + step.y)
    ```

   Also note that we are moving to the north by default and that this implies
   a step (or increment if you will) of ``[0 1]``. This suggests yet another generalization,
   namely a directions enumeration

   ```python
   class Direction(Enum):
     NORTH = [ 0,  1]
     EAST =  [ 1,  0]
     SOUTH = [ 0, -1]
     WEST =  [-1,  0]
   ```

   This implies that the ``move_forward()`` method can be rewritten as

   ```python
   def move_forward(self):
     self.coordinates = self.coordinates.add(Coordinates(Direction.NORTH.value[0], Direction.NORTH.value[1]))
   ```

   Finally, we may further want to generalize this by introducing a direction property
   into the rover, which associated increments we can then use when moving either forwards or backwards.

4. Next we want to be able to turn left and right. Let's start with a turn to the right

   ```python 
   with it("moves to the east after a right turn"):
     self.rover.turn_right()
     self.rover.move_forward()
     expect(self.rover.is_at()).to(equal(Coordinates(1, 0)))
   ```

   We can easily make it green by hard-coding the new direction in the ``turn-right()`` implementation.
     
5. Next up is a turn to the left

   ```python 
   with it("moves to the west after a left turn"):
     self.rover.turn_left()
     self.rover.move_forward()
     expect(self.rover.is_at()).to(equal(Coordinates(-1, 0)))
   ```

   We can easily make it green by hard-coding the new direction in the ``turn-left()`` implementation.

6. We invalidate the hard-coded implementations of the turn-methods by adding the following test

   ```python
   with it("moves to the north after a left and right turn"):
     self.rover.turn_left()
     self.rover.turn_right()
     self.rover.move_forward()
     expect(self.rover.is_at()).to(equal(Coordinates(0, 1)))
   ```

   This can be solved by introducing new methods on the ``Direction`` enumeration

   ```python
   @staticmethod
   def to_the_right_of(direction):
     index = list(Direction).index(direction) + 1
     return list(Direction)[index if index <= 3 else 0]

   @staticmethod
   def to_the_left_of(direction):
     index = list(Direction).index(direction) - 1
     return list(Direction)[index if index >= 0 else 3]
  ```


