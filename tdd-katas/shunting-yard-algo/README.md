# Introduction

The [shunting yard algorithm](https://en.wikipedia.org/wiki/Shunting_yard_algorithm)
is a method to convert expression in the infix notation to expression in the postfix
notation, also known as 
[reverse Polish notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation) (RPN).

The advantage is that RPN removes the need for parentheses. Lisp dialects such as Clojure
employ a prefix notation by default, since all operations are defined as functions:

```clojure
(println (+ 3 4))
```

The idea is to develop a relatively complex algorithm using TDD techniques and
principles.
