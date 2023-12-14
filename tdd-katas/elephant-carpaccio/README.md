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

## References

- [Facilitation guide by Henrik Kniberg &amp; Alistair Cockburn](https://docs.google.com/document/d/1TCuuu-8Mm14oxsOnlk8DqfZAA1cvtYu9WGv67Yj_sSk/pub)
- [Slide deck by Michael Wallace](https://static1.squarespace.com/static/59e39ba7268b9625f429cc67/t/5a37ed1124a6949ae31ae169/1513614612707/Elephant-Carpaccio_november2017_chapter-presentation.pdf)
- [Two times remote Elephant Carpaccio](https://smallsheds.garden/blog/2021/two-times-remote-elephant-carpaccio/)
