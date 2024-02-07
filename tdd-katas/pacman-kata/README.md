![Pacman](pacman.jpg)

# Introduction

The Pacman kata practices a more complex real-world scenario that entails challenges such as incorporating external frameworks (gaming engine) and a rich-client application that runs on a desktop. 

In addition, this kata brings together quite a few techniques that we practiced in other katas such as

- Steering Pacman left, right, up, and, down much like we did in the [mars rover kata](../mars-rover)
- Applying [ports and adapters](https://github.com/zhendrikse/tdd/wiki/Hexagonal-Architecture) to isolate all the calls to the gaming engine framework
- Determining the distances in the Pacman maze by using the [manhattan distance](../manhattan-distance)
- Working with nodes and neighbors on a game board much like we do in the [game of life](../game-of-life)

# Suggestions

1. Use the [cookiecutter template for test-driven development of (Python) games](https://github.com/zhendrikse/tdd/tree/master/cookiecutter)  
2. Start by creating a maze consisting from nodes and vertices. It is preferred to construct this set of connected nodes from file or string, since the ultimate maze(s) will be way too difficult to set up manually.

   ```
   X X X X X X X X
   X + . . + X X X
   X . X X . X X X
   X + . . + . + X
   X . X X X X . X
   X . X X X X . X
   X + . . . . + X
   X X X X X X X X
   ```
   Further details can de found [here](https://pacmancode.com/maze-basics).
5. Make Pacman move along the nodes and vertices of this maze, as explained [here](https://pacmancode.com/node-movement-part-1)
6. Add the pellets and eat them
7. Add the ghosts by giving them random movements
8. Etc.

# References

- [pacmancode.com](https://pacmancode.com)
