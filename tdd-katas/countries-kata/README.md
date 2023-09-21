# Introduction

This is a kata designed to teach you how to keep your system 
under development properly testable when dealing with interactions 
with external systems, in this case, REST endpoints, and writing
output to files using
[the ports &amp; adapter architecture and dependency inversion](https://github.com/zhendrikse/tdd/wiki/Hexagonal-Architecture).

We are going to implement a converter that consumes some country data
from a REST API on the web, enrich those data (a bit), and then 
export those data to CSV.

This kata shows how to drive the realization of this application
from the inside out, rather than starting from the external data provider 
by first focusing on the domain logic. Eventually, we connect the
domain to the outside world using ports &amp; adapters.

## The domain logic that is requested

Given a list of countries (with some data per country such 
as name, population, and capital city), we are interested in getting 
an overview of all countries in the world, sorted by the 
size of their population in ascending order. In addition, 
we would like to know for each country how many standard deviations
its population deviates from the world's average population size. 

### Example of expected output 

The output should be a CSV file:

```
name,capital,population,deviation
Belgium,Brussels,3,0.40
Netherlands,Amsterdam,4,0.73
Portugal,Lissabon,7,0.37
United Kingdom,London,10,1.46 
```

### Country data retrieval

A list with 
[country information](https://restcountries.com/v3.1/all?fields=name,capital,population,cioc,region) 
is obtained from the [REST countries API](https://restcountries.com/). 
The endpoint _intentionally_ delivers more fields than we are interested in!

### Doing the math 

If unsure about how to calculate the numbers, you can go to any 
[online standard deviation calculator](https://www.mathsisfun.com/data/standard-deviation-calculator.html).

Using the numbers from the example (3, 4, 7, 10), we arrive at a mean
of 24 / 4 = 6, with a standard deviation of 2.738612788.

We see that the first number differs 3 from the mean, which is approximately 1.095 standard deviations.
hint: you can use numpy to calulate the mean and standard deviation (std).

Example calculation:

| population | difference    | std         | deviation   |
|------------|---------------|-------------|-------------|
| 3          | abs(6-3) = 3  | 2.738612788 | 1.095445115 |
| 4          | abs(6-4) = 2  | 2.738612788 | 0.730296743 |
| 7          | abs(6-7) = 1  | 2.738612788 | 0.365148372 |
| 10         | abs(6-10) = 4 | 2.738612788 | 1.460593486 |


**Caveat**: 
Note that the API returns the capital city in a list, and sometimes 
this list may even be empty!

## Kata as legacy or greenfield

There are two options to practice this kata:

1. Approach it as a legacy application, that has no tests yet.
   The exercise is to make this application better
   testable by refactoring it to include ports &amp; adapters.
   Both the CSV writer as well as the retrieval of country data
   should be handled using adapters.
2. Approach it as a greenfield application, that has to be written from the
   ground up.

The goal is not to complete this kata as quickly as possible, 
but to follow the rules of ports &amp; adapters architecture:

- The domain logic itself does not depend directly on
  any of the external systems, but only on ports
- The protocol for a port is given by the purpose of 
  the conversation that it describes.
- For each external system there is an adapter that converts
  the API definition to the format 
  needed by that system and vice versa.

## Optional extensions

- Add a possibility to filter, e.g. only export those countries to CSV that
  are a UN member, or only export those countries that have more than 10 million
  inhabitants.
- Add a possibility to update a reference table in a database with these
  country data. Optionally according to a certain time schedule, e.g. weekly.

## References

- [Ports and adapters as they should be](https://medium.com/wearewaes/ports-and-adapters-as-they-should-be-6aa5da8893b)
