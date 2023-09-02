class Coordinate {
    private x: number
    private y: number  
  
    constructor(x: number, y: number) {
      this.x = x
      this.y = y
    }
  
    decrement(increment: Coordinate): Coordinate {
      return new Coordinate(this.x - increment.x, this.y - increment.y)
    } 
  
    increment(increment: Coordinate): Coordinate {
      return new Coordinate(this.x + increment.x, this.y + increment.y)
    } 
  
    asArray(): [number, number] {
      return [this.x, this.y]
    }
  }
  
  enum Direction {
    NORTH = 0,
    EAST =  1,
    SOUTH = 2,
    WEST =  3,
    UNDEFINED = 4
  }
  
  const directionSteps: Map<Direction, Coordinate> = new Map ([
    [Direction.NORTH, new Coordinate( 0,  1)],
    [Direction.SOUTH, new Coordinate( 0, -1)],
    [Direction.EAST,  new Coordinate( 1,  0)],
    [Direction.WEST,  new Coordinate(-1,  0)]    
  ])
  
  class Rover {
    private position: Coordinate = new Coordinate(0, 0)  
    private direction: Direction = Direction.NORTH
    
    isAt(): [number, number] {
      return this.position.asArray()
    }
  
    moveForward() {
      this.position = this.position.increment(directionSteps.get(this.direction) as Coordinate)
    }
  
    moveBackward() {
      this.position = this.position.decrement(directionSteps.get(this.direction) as Coordinate)
    }
  
    turnLeft() {
      this.turnRight(); this.turnRight(); this.turnRight()
    }
  
    turnRight() {
      this.direction += 1
      if (this.direction == Direction.UNDEFINED) this.direction = Direction.NORTH
    }
  
    receiveCommandString(command: String) {
      for (var char of command) {
        if (char == "f") this.moveForward()
      }
    }
  }
  
  export {Rover};
  export {Rover as rover};
  