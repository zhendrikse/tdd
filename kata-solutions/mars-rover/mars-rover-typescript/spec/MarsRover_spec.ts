import { expect, assert } from "chai"
import { Rover } from '../src/MarsRover';

describe("Mars rover", () => {
  let marsRover: Rover;

  beforeEach(() => {
    marsRover = new Rover()
  })

  it("starts at position (0, 0)", () => {
    expect(marsRover.isAt()).to.have.same.members([0, 0])
  })

  it("moves forward to the north", () => {
    marsRover.moveForward()
    expect(marsRover.isAt()).to.have.same.members([0, 1])
  })

  it("moves backward to the south", () => {
    marsRover.moveBackward()
    expect(marsRover.isAt()).to.have.same.members([0, -1])
  })

  it("moves 2 steps forwards to the north", () => {
    marsRover.moveForward()
    marsRover.moveForward()
    expect(marsRover.isAt()).to.have.same.members([0, 2])
  })

  it("moves 1 step forwards to the east after a right turn", () => {
    marsRover.turnRight()
    marsRover.moveForward()
    expect(marsRover.isAt()).to.have.same.members([1, 0])
  })

  it("moves 1 step backwards to the west after a right turn", () => {
    marsRover.turnRight()
    marsRover.moveBackward()
    expect(marsRover.isAt()).to.have.same.members([-1, 0])
  })
  
  it("moves 1 step forwards to the south after a double left turn", () => {
    marsRover.turnLeft()
    marsRover.turnLeft()
    marsRover.moveForward()
    expect(marsRover.isAt()).to.have.same.members([0, -1])
  })

  it("does not move when an empty command string is entered", () => {
    marsRover.receiveCommandString("")
    expect(marsRover.isAt()).to.have.same.members([0, 0])
  })

  it("moves 1 step forwards when command string 'f' is entered", () => {
    marsRover.receiveCommandString("f")
    expect(marsRover.isAt()).to.have.same.members([0, 1])
  })

  it("moves 3 steps forwards when command string 'fff' is entered", () => {
    marsRover.receiveCommandString("fff")
    expect(marsRover.isAt()).to.have.same.members([0, 3])
  })
})