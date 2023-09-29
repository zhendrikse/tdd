from mamba import description, it, context, before
from expects import expect, be, raise_error, be_true, be_false, equal
from enum import Enum
from dataclasses import dataclass


@dataclass(frozen=True)
class Coordinates:
    x: int
    y: int

    def add(self, step):
        return Coordinates(self.x + step.x, self.y + step.y)


class Direction(Enum):
    NORTH = [0, 1]
    EAST = [1, 0]
    SOUTH = [0, -1]
    WEST = [-1, 0]

    @staticmethod
    def to_the_right_of(direction):
        index = list(Direction).index(direction) + 1
        return list(Direction)[index if index <= 3 else 0]

    @staticmethod
    def to_the_left_of(direction):
        index = list(Direction).index(direction) - 1
        return list(Direction)[index if index >= 0 else 3]


class Rover:

    def __init__(self, _coordinates=Coordinates(0, 0)):
        self._coordinates = _coordinates
        self._direction = Direction.NORTH

    def is_at(self):
        return self._coordinates

    def move_forward(self):
        self._coordinates = self._coordinates.add(
            Coordinates(self._direction.value[0], self._direction.value[1]))

    def move_backward(self):
        self._coordinates = self._coordinates.add(
            Coordinates(-self._direction.value[0], -self._direction.value[1]))

    def turn_right(self):
        self._direction = Direction.to_the_right_of(self._direction)

    def turn_left(self):
        self._direction = Direction.to_the_left_of(self._direction)


with description(Rover) as self:
    with before.each:
        self.rover = Rover()

    with it("starts at position (0, 0)"):
        expect(self.rover.is_at()).to(equal(Coordinates(0, 0)))

    with it("moves one step forward to the north by default"):
        self.rover.move_forward()
        expect(self.rover.is_at()).to(equal(Coordinates(0, 1)))

    with it("moves one step backward to the south by default"):
        self.rover.move_backward()
        expect(self.rover.is_at()).to(equal(Coordinates(0, -1)))

    with it("moves one step to the east after a right turn"):
        self.rover.turn_right()
        self.rover.move_forward()
        expect(self.rover.is_at()).to(equal(Coordinates(1, 0)))

    with it("moves one step to the east after a left turn"):
        self.rover.turn_left()
        self.rover.move_forward()
        expect(self.rover.is_at()).to(equal(Coordinates(-1, 0)))

    with it("moves one step to the north after a left and right turn"):
        self.rover.turn_left()
        self.rover.turn_right()
        self.rover.move_forward()
        expect(self.rover.is_at()).to(equal(Coordinates(0, 1)))
