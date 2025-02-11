{% include breadcrumbs.html %}

# What coding katas are about
<div class="header_line"><br/></div>

> Japanese culture influenced a lot of software and project management fields. 
> Concepts like [Lean](https://apiumhub.com/?p=55302), [Kata](https://apiumhub.com/?p=4044), etc 
> has come from Japan. And we should admit, that they have improved the existing processes, 
> increasing efficiency and satisfaction overall &#8212; [apiumhub.com](https://apiumhub.com/tech-blog-barcelona/code-kata/)

With the materials in this repository, you'll learn TDD by practicing 
so-called [coding katas](https://apiumhub.com/tech-blog-barcelona/code-kata/):

![Kata](https://github.com/zhendrikse/tdd/blob/master/assets/kata.png?raw=true)

> A kata is an exercise in karate where you repeat a form many, many times, making little improvements in each. 
> The intent behind code kata is similar &#8212; [codekata.com](http://codekata.com/) 

Generally speaking, each kata tries to target one or more skills, 
and this collection is no exception to that general rule. As the saying goes, 
practice makes perfect, and the same holds for (coding) katas: preferably 
you make them your own by repeating them _time and again_.

Although the saying goes that practice makes perfect, the reality is 
that code almost never reaches a perfect state: you can always find ways to 
further improve your code and your skill(s). There are always new ways to become 
more proficient and faster. Luckily, it turns out that mastery is one of
[the three primary drivers that keep us motivated](https://www.youtube.com/watch?v=u6XAPnuFjJc). 
Moreover, the payoff of mastering TDD is much higher than the investments that you'll put in. 

After spending a certain time with TDD, people claim that there is no 
other way to develop software. It is almost a learning to type with ten 
fingers: once you master the skill, you wonder how you ever managed without it.

# Katas using backtracking algorithms

For a couple of katas such as the Sudoku solver, we need to implement a backtracking algorithm.
So let's elaborate a bit on this topic.

## A simple backtracking example in Clojure

This section is based on 
[the Sudoku exercise](http://iloveponies.github.io/120-hour-epic-sax-marathon/sudoku.html)
that is part of the Clojure course at the Department of Computer Science at the 
University of Helsinki.

Subset sum is a classic problem. You are given a set of numbers, 
such as the set `#{1 2 10 5 7}` and another number, let's say `23`.

The problem is to find out if there is a subset of the original set that has a sum equal to the target number.

Let's see how we can solve this by implementing a brute-force approach based on a backtracking search.

Here's a possible implementation:

```clojure
(defn sum-from [a-sequence]
  (reduce + a-sequence))

(defn sum-from? [a-set has-target-sum]
  (= (sum-from a-set) has-target-sum))

(defn subset-from [a-set subset-probe has-target-sum]
  (if (sum-from? subset-probe has-target-sum)
    [subset-probe]
    (let [remaining-elements (clojure.set/difference a-set subset-probe)]
      (for [element remaining-elements
            solution (subset-from a-set
                                  (conj subset-probe element)
                                  has-target-sum)]
        solution))))

(defn subsets-from [a-set with-target-sum]
  (subset-from a-set #{} with-target-sum))
```

So the main thing that happens inside `subset-from`. 
We check if we have found a valid solution with the function

```clojure
  (if (sum-from? subset-probe has-target-sum)
    [subset-probe]
```

If the current subset probe is a valid solution, 
we return it in a vector (we’ll see soon why in a vector). 

If the current subset probe is not a valid solution, 
we need to try adding another element of `a-set` to the 
`subset-probe` and try again. 

Which elements are eligible for this? 
Those elements that are not yet in `subset-probe`. 
Those are bound to the name `remaining-elements` here:

```clojure
    (let [remaining-elements (clojure.set/difference a-set subset-probe)]
```

What’s left is to actually try calling `subset-from` with each 
new set obtainable in this way:

```clojure
      (for [element remaining-elements
            solution (subset-from a-set
                                  (conj subset-probe element)
                                  has-target-sum)]
        solution))))
```

Here first `element` gets bound to the elements of `remaining-elements` one at a time.
For each `element`, `solution` gets bound to each element of the recursive call.

```clojure
            solution (subset-from a-set
                                  (conj subset-probe element)
                                  has-target-sum)]
```

This is the reason we returned a vector in the base case so 
that we can use `for` in this way. 

Finally, we return each such `solution` in a sequence.

So let’s try this out:

```clojure
user=> (def with-target-sum-of identity)
user=> (subsets-from #{1 3 4 10 9 23} (with-target-sum-of 20))
;=> (#{1 9 10} #{1 9 10} #{1 9 10} #{1 9 10} #{1 9 10} #{1 9 10})
```

Okay, so the example above is not exactly optimal. 
It forms each set many times. 
Since we are only interested in one solution, 
we can just add `first` to the call to
the `subset-from` function:

```clojure
(defn subsets-from [a-set with-target-sum]
  (first subset-from a-set #{} with-target-sum)))
```

And because of the way Clojure uses laziness, 
this actually shortens the computation after a solution has been found 
(well, to be precise, after 32 solutions have been found, due to the way 
the way Clojure chunks lazy sequences).

## References

- [A curated list of programming katas](https://hackmd.io/@pierodibello/A-curated-list-of-programming-kata#A-curated-list-of-programming-kata)
- [Awesome katas](https://github.com/gamontal/awesome-katas#readme)
- [Kata-Log](https://kata-log.rocks/)
