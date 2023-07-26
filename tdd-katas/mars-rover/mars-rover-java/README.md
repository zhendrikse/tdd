# Introduction

Please read the general [introduction to the mars rover kata](../README.md) first!

# Teaser

We are going to implement the Mars rover using the functional programming
paradigm, thereby respecting the strict constraints that are mentioned in the
[introduction to the mars rover kata](../README.md)!

```java
public void processCommands(String commands) {
  this.state = Arrays
    .stream(commands.split(""))
    .map(Command::fromChar)
    .map(Rover.implementationMap::get)
    .map(Rover::curryWithMoveVector)
    .reduce(Function.identity(), Function::andThen)
    .apply(state);
}
```

The approach here is an almost literral TDD version of the 
excellent functional solution that can be foudn in this
[code repository](https://github.com/davidibl/MarsRover/tree/master).

# Getting started

First, create an intial Java kata set-up as described [here](https://github.com/zhendrikse/tdd/tree/master/cookiecutter).

Next, go the the newly created project directory and consult
the provided ``README.md`` in there.

# Functional implementation

TODO