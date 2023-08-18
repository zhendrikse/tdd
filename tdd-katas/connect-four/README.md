# Connect 4

```
Computer plays 1
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|🟡|  |  |🔴|  |  |  |
  1  2  3  4  5  6  7 
Enter your row: 
```

## Definitions

- Two players: RED and YELLOW
- RED always starts
- A board has 7 columns and 6 rows
- First column is column number 1

## Setting up a configuration

This means that the string "4433562" leads to the following configuration:

```
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 2 2 0 0 0
0 1 1 1 1 2 0
```

## Links


### Board representations

- [Bitboards and Connect Four](https://github.com/denkspuren/BitboardC4/blob/master/BitboardDesign.md)

### Languages

- [Connect 4 in Clojure](https://github.com/eigenlicht/clj-connect-four), good code but without tests

### Algorithms

- [Constructing Agents for Connect-4: Initial Notes](https://markusthill.github.io/programming/connect-4-introduction-and-tree-search-algorithms/)
- [Solving connect four: how to build a perfect AI](http://blog.gamesolver.org/solving-connect-four/01-introduction/)
- [Artificial Intelligence at Play — Connect Four (Mini-max algorithm explained)](https://medium.com/analytics-vidhya/artificial-intelligence-at-play-connect-four-minimax-algorithm-explained-3b5fc32e4a4f)
- [Creating the (nearly) perfect connect-four bot with limited move time and file size](https://towardsdatascience.com/creating-the-perfect-connect-four-ai-bot-c165115557b0)
- [How to teach your robot to play connect four](https://roboticsproject.readthedocs.io/en/latest/index.html)
- [Connect 4 AI: How it works](https://roadtolarissa.com/connect-4-ai-how-it-works/)
- https://markusthill.github.io/programming/connect-4-transposition-tables/
