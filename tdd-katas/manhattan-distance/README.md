![Manhattan](./assets/manhattan.png)

# The Manhattan distance kata

In this kata, you will learn about another important TDD principle, namely the 1-2-N princple, also known as [three strikes and you refactor](http://wiki.c2.com/?ThreeStrikesAndYouRefactor). This means that before you implement a generic case (_N = n_), you first implement the case for _N = 1_, then the case for _N = 2_, and finally generalize it to _N = n_.

In this kata, you will first calculate the [Manhattan distance](http://en.wikipedia.org/wiki/Manhattan_distance) between two points in a one-dimensional space (i.e. on a line), and then two points in a plane. Next, you'll be able to generalize it to points located in _N_-dimensional spaces.

## The Manhattan distance 

![Manhattan distance](./assets/Manhattan_distance.png)
<p align="center" ><b>Figure 1</b>: <i>The Manhattan distance is independent of the chosen route and is defined as the sum of the absolute differences in both the x and y coordinates between both points.</i></p>

The [Manhattan distance](http://en.wikipedia.org/wiki/Manhattan_distance) is the distance between two points in a grid (like the grid-like street geography of the New York borough of Manhattan) calculated by only taking a vertical and/or horizontal path.

The distance only depends on the absolute difference in the _x_ and _y_ coordinates. It does _not_ depend on a particular route that is taken.

You are going to write a function `int manhattanDistance(Point, Point)` that returns the Manhattan Distance between the two points. From the beginning, it will be our intention to generalize the distance to _N_ dimensions.

## Rules

It is extremely important to "play" this kata by the rules, as it also aims to show how to avoid exposing state of a class and instead, implement behavior that logically belongs to this state in that same class (remember: [object = state + behavior + identity](https://newbedev.com/trouble-understanding-object-state-behavior-and-identity), also known as [tell don't ask](https://martinfowler.com/bliki/TellDontAsk.html) principle).

So summarizing, the following rules need to be applied:
- The class `Point` is immutable (its state cannot be changed after instantiation)
- The class `Point` has no getters for the coordinates
- The class `Point` has no public properties (i.e. the internal state cannot be read nor modified from outside the class).

## Optional extension

# Optional: determine all shortest paths

For those that are up to a more challenging extension: determine the number of possible shortest paths when the points are two-dimensional (see [this web page](https://www.robertdickau.com/manhattan.html) for a nice graphical representation when the horizontal and vertical distances are equal).   

A somewhat more complex extension would be to output all paths explicitly in a sequence of steps, where `u` is up, `d` is down, `l` is left, and `r` is right. A typical output for two points separated 3 blocks horizontally and 2 vertically would then look something like

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
