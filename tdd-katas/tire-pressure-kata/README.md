# Tire Pressure Code Kata

A copy of Emily Bache's [tire pressure kata](https://github.com/emilybache/Racing-Car-Katas/tree/main/Python/TirePressureMonitoringSystem), part of the so-called
[racing car katas](https://github.com/emilybache/Racing-Car-Katas/tree/main).

The idea is to test whether or not the alarm goes off whenever the tire pressure
happens to go beyond the (hard-coded) boundaries.

# Possible approaches

There are almost countless ways of approaching this task/kata. 
Some possibilities are mentioned below.

## Option 1: peel strategy

The [peel strategy](https://www.sammancoaching.org/learning_hours/testable_design/peel.html)
is explained by [Emily Bache](https://github.com/emilybache) 
([https://www.sammancoaching.org/](https://www.sammancoaching.org/)).

## Option 2: slice strategy

The [slice strategy](https://www.sammancoaching.org/learning_hours/testable_design/slice.html)
is explained by [Emily Bache](https://github.com/emilybache) 
([https://www.sammancoaching.org/](https://www.sammancoaching.org/)).

## Option 3: ports &amp; adapters

The [ports &amp; adapters](https://alistair.cockburn.us/hexagonal-architecture/)
approach can frequently be used in these kinds of situations.

If we allow ourselves to modify the code, we can create an interface 
for the tire pressure sensor and have the alarm class depend on that 
interface instead of the concrete sensor class. The interface can then
easily be stubbed.

## Option 4: Language-specific approaches

### Monkey patching

For dynamic languages, we can use [monkey patching](https://en.wikipedia.org/wiki/Monkey_patch).
