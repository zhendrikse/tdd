# Introduction

The [shunting yard algorithm](https://en.wikipedia.org/wiki/Shunting_yard_algorithm)
is a method to convert expressions from the infix notation to expressions in the postfix
notation, also known as 
[reverse Polish notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation) (RPN).

The advantage is that the RPN removes the need for parentheses. Lisp dialects such as Clojure
employ a prefix notation, since all operations are defined as functions:

```clojure
(println (+ 3 4))
```

The idea of this kata is to develop a relatively complex algorithm using TDD techniques and
principles.
