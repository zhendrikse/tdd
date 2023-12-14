# Elephant Carpaccio Kata

![Elephant carpaccio](images/sliced_elephant.png)

Original content is taken from [Alistair Cockburn's PDF](https://alistair.cockburn.us/wp-content/uploads/2018/02/Elephant-Carpaccio-exercise-instructions.pdf).

## Learning outcomes 

- How to slice large applications into 1-day to 
  1-week requests, business perspective 
- How to slice application requests into 15-30 minute 
  work slices, programming perspective

## Instructions

1. Break into teams of 2-3 people, one workstation per team.
2. **10 minutes**: Preparation 
   - Each team writes down on paper the 10-20 demo-able user 
     stories ("slices") they will develop and possibly demo. 
   - Each story should be doable in 3-8 minutes. 
   - No slice is just a mockup of a UI, the creation of a data table 
     or data structure. 
   - All demos show real input & output (not test harness).
3. **15 minutes**: Discussion 
   - Instructor/facilitator leads discussion of the slices, 
     what is and isn't acceptable, and solicits ways to slice finer.
4. **40 minutes**: Development 
   - A fixed time-box of 40 minutes, five 8-minute development sprints,
     the clock does not stop. At the end of each sprint, each team shows its 
     product to another team.
5. Debrief

## Assignment

Accept 4 inputs from the user:
- number of items, 
- a price, 
- a 2-letter state code,
- a date (only for spreadsheets)

## Stage 1

Create a 1-line calculator that computes the price of the order, 
giving a discount based on the order value (not number of items), 
adding state tax based on the state and the discounted order value.

| Order value | Discount rate | State Tax rate |
|:----------- |:------------- |:-------------- |
| $ 1,000     |  3 %          | UT 6.85 %      |
| $ 5,000     |  5 %          | NV 8.00 %      |
| $ 7,000     |  7 %          | TX 6.25 %      |
| $10,000     | 10 %          | AL 4.00 %      |
| $50,000     | 15 %          | CA 8.25 %      |

## Stage 2 for spreadsheets only:

Create a set of orders from different months and different states.

Produce a report as a histogram of sales results by state, 
then a second sales report histogram of sales
results by month.

Create a PowerPoint presentation that shows your sponsors what you 
have created, with the formula you used, sample inputs and outputs, 
the sales history and the graphs.

# Additional background information

## Splitting stories

A user story is preferably [INVEST](https://www.agilealliance.org/glossary/invest/)
- “I” ndependent (of all others)
- “N” egotiable (not a specific contract for features)
- “V” aluable (or vertical)
- “E” stimable (to a good approximation)
- “S” mall (so as to fit within an iteration)
- “T” estable (in principle, even if there isn’t a test for it yet)

It is especially the "Vertical", "Small", and "Testable" that we are interested in
during this kata, although "Negotiable" can sometimes be applied as well!

The challenge is to always slice user stories _vertically_, so that each user
story adds some value, however small that added value may be!

![vertical user stories](./images/vertical_user_stories.png)

Story slicing boils down to the art of making the slices as thin as possible
_while at the same time_ retaining business value for each slice

![sliced user stories](./images/sliced_user_stories.png)

This is of utmost importance, as the value delivered is maximized as early as
possible. This is caused by the fact that frequent and early delivery 
enables users to use to product much sooner and thus providing the opportunity
to give feedback as well as reprioritization requests to the product owner. 

![vertical user stories](./images/value_delivered.png)

## Priorities

### The ultimate target

![Prio 1](./images/five_states_five_discounts_1.png)

### The taxes first

The product owner wants 5 states before doing anything with discounts. 
Why? (so we can deploy! State tax is a legal requirement, discount is not)

![Prio 2](./images/five_states_five_discounts_2.png)

### Validation &amp; fancy GUI comes after 5 states &amp; 5 discounts

A (fancy) GUI is of the _least_ importance! As long as the prices and taxes
of the products can be determined, the products can be sold. The longer we
wait for the fancy GUI, the more we miss out on our revenues!

![Prio 3](./images/five_states_five_discounts_3.png)

### Coarse-grained slicing strategy

Concluding, a good slicing strategy will roughly look as follows:

![Prio 4](./images/five_states_five_discounts_4.png)



# References

- [Facilitation guide by Henrik Kniberg &amp; Alistair Cockburn](https://docs.google.com/document/d/1TCuuu-8Mm14oxsOnlk8DqfZAA1cvtYu9WGv67Yj_sSk/pub)
- [Slide deck by Michael Wallace](https://static1.squarespace.com/static/59e39ba7268b9625f429cc67/t/5a37ed1124a6949ae31ae169/1513614612707/Elephant-Carpaccio_november2017_chapter-presentation.pdf)
- [Two times remote Elephant Carpaccio](https://smallsheds.garden/blog/2021/two-times-remote-elephant-carpaccio/)
