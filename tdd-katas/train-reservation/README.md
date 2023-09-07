# Train reservation kata

## Goal

The emphasis in this kata is on practicing/getting acquainted with 
[double-loop TDD](https://sammancoaching.org/learning_hours/bdd/double_loop_tdd.html)
using example mapping as a means to formulate the test(s) in the outer loop.

## Task

The assignment in this kata is to build a reservation system for
train tickets based on the following business rules

- 70% of maximum train capacity can be reserved in advance
- All seats of one reservation must be in the same coach
- Ideally, all coaches have 70% occupation

In case you want to make it even more complex, you may want
to impose an additional rule

- Ideally, all persons that are part of a single reservation
  should be seated together as closely as possible.

The size nor the lay-out of the coaches is given, but a typical lay-out
could look like this:

![Sample configuration](./images/train-reservation-kata.png)

# Introduction Example mapping

The image below is based on the [Scrumblr](http://scrumblr.ca/) board running in 
[this replit repository](https://scrumblr.zwh.repl.co/Example%20mapping). 
If you're entering from the main page, the board is called "Example mapping".

![Example mapping](./images/example-mapping.png)


## References

- [Introduction video](https://www.youtube.com/watch?v=VwvrGfWmG_U) to example mapping
- Short [blog post](https://cucumber.io/blog/bdd/example-mapping-introduction/)
- [Prepared online board](https://scrumblr.zwh.repl.co/Example%20mapping) that can be used
- Based on the instructions and code found in the [repo of Emily Bache](https://github.com/emilybache/KataTrainReservation/tree/master#readme)
