# Train reservation kata

The assignment in this kata is to build a reservation system for
train tickets based on a set of business rules.

## Goal

The emphasis in this kata is on practicing/getting acquainted with 
[double-loop TDD](https://sammancoaching.org/learning_hours/bdd/double_loop_tdd.html)
using example mapping as a means to formulate the acceptance test(s) in the outer loop.
You may want to learn more about example mapping on the
[example mapping](https://github.com/zhendrikse/tdd/wiki/Example-mapping) Wiki page.

![Double loop TDD](../../presentations/intro-tdd/images/tdd-scope.png)

The features/business rules/acceptance criteria that are collected using the
example mapping technique can _directly_ be translated into 
[Gherkin](https://cucumber.io/docs/gherkin/) feature files:


```
Feature: Booking seats on a train from the ticket office

  Scenario: Listing available trains
    Given There are trains available
    When I ask for trains
    Then I get a list of trains
``` 

These feature files in turn can easily be connected to the production code
base by implementing fixtures in so-called step files. Some well-known
frameworks that support this approach are [Cucumber](https://cucumber.io/) and
[SpecFlow](https://specflow.org/).


## Business Rules

The user story is pretty straightforward:

> *As* a passenger
> *I want to* book a train ticket in advance
> *so that* I can count on it with my planning.

When facilitating the example mapping workshop, you can choose between
a couple of different approaches/profiles.

### Profile 1: The One With Last-Minute Bookings

- 3 rules are introduced at the same time.<br/>
  ⇒ All seats for one reservation in the same coach.<br/> 
  ⇒ Max 70% of the entire train.<br/>
  ⇒ Ideally, max 70% of each coach.
- We want to keep seats for last-minute bookings because they are valuable (10% more expensive).
- We want to distribute bookings for security reasons.

### Profile 2: The One With Hidden Discounts

- 3 rules introduced one by one.<br/>
  ⇒ All seats for one reservation in the same coach.<br/>
  ⇒ Max 70% of the entire train.<br/>
  ⇒ Ideally, max 70% of each coach.
- We want to keep seats for last-minute bookings because they are valuable (10% more expensive).
- At most 8 seats per reservation because you benefit from a 5% discount starting from 6 seats per reservation.

### Profile 3: The One With Overbooking

- No rules are introduced at all. There is only one sketched example illustrating the following rule:<br/>
  ⇒ All seats for one reservation in the same coach.
- We don’t care about the distribution of bookings across the train.
- We accept overbooking as you don’t need to have a seat to take the train!

### Profile 4: The One With High-Comfort Standards

- No rules are introduced at all. There is only one sketched example illustrating the following rule:<br/>
  ⇒ All seats for one reservation in the same coach.
- We don’t care about the distribution of bookings across the train.
- We refuse overbooking as we have high comfort standards.
- You can choose specific locations across the train (window, aisle, duo).

The size nor the layout of the coaches is given, but a typical layout
could look like this:

![Sample configuration](./images/train-reservation-kata.png)

## Tips

You may want to consider the following scenarios when formulating the examples:

- Booking when less than 70% occupancy is inevitable
- Booking for single persons
- Booking for multiple persons
- Same coach reservation
- Multiple coach reservation
- Conflicts

An example of another user story (ticket cancellation) is detailed on the
[example mapping](https://github.com/zhendrikse/tdd/wiki/Example-mapping) Wiki page.


## References

- This kata is inspired by the version of this kata found in the [repo of Emily Bache](https://github.com/emilybache/KataTrainReservation/tree/master#readme)
- Modeling the train reservation kata
  [part 1](https://sadraskol.com/posts/modeling-the-train-reservation-kata-part-1/) and
  [part 2](https://sadraskol.com/posts/modeling-the-train-reservation-kata-part-2/)
