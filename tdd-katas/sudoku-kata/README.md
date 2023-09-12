![Sudoku](./assets/sudoku.jpg)

# Sudoku kata

In this kata, we are going to write a Sodoku solver.
The rules for Sudoku are:

- Every square has to contain a single number.
- Only the numbers from 1 through to 9 can be used.
- Each 3×3 box can only contain a number from 1 to 9 once and only once.
- Each vertical column can only contain each number from 1 to 9 once.

## Possible approaches

Practicing this kata pays off the most when it is done multiple times in 
multiple different ways. Many people have already written about such approaches:

- [Solving every Sudoku puzzle](http://norvig.com/sudoku.html) by Peter Norvig and
  references contained therein.
- [TDD Practice #2: The Sudoku Example in Clojure – Starting the Unit Testing](https://www.linkedin.com/pulse/tdd-practice-2-sudoku-example-clojure-starting-unit-testing-viana-/)
  outlines a _strict_ TDD approach using the [Transformation Priority Premise](https://blog.cleancoder.com/uncle-bob/2013/05/27/TheTransformationPriorityPremise.html).
  This approach clearly shows how to incrementally develop a recursive algorithm.
- Brute force approaches often rely on some form of [backtraching](https://github.com/zhendrikse/tdd/wiki/Coding-Katas#katas-using-backtracking-algorithms).
  The idea is to let the computer solve Sudoku puzzles using a brute-force approach. However, by using backtracking, we ensure that invalid branches are pruned early.
  

In the Java and Python versions (i.e. based on the OO paradigm), there 
is an option to exercise with the [data clumping](https://refactoring.guru/smells/data-clumps) refactoring 
that is applicable to the pervasive grouping of the row and column parameters.

