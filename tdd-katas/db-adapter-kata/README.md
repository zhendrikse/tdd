# How to deal with external systems

In this module we are going to build a very basic REST API that fetches employee data from a database and stores these data into a database.

![REST API](./assets/RestAPI.draw)
<p align="center" ><b>Figure 1</b>: <i>A schematic representation of the application that we are going to build.</i></p>

Note that the above lay-out can be seen as a simplification of the aforementioned hexagonal architecture:

![Hexagonal architecture](./assets/hex_arch.draw)
<p align="center" ><b>Figure 2</b>: <i>A schematic representation of the hexagonal architecture.</i></p>

As the domain logic will (almost) be absent in this kata, this implies we can simplify the picture of the hexagonal architecture as shown in the first picture. Note that normally this will almost never be the case, but the purpose of this exercise is to learn how to implement an adapter, not (even some simple form of) a [domain model](https://matfrs2.github.io/RS2/predavanja/literatura/Avram%20A,%20Marinescu%20F.%20-%20Domain%20Driven%20Design%20Quickly.pdf). 

So summarizing, we are going to focus on how to deal with test doubles and external systems, in this case a database. 

# The kata

In this kata, we are going to implement the following endpoints:

![Endpoints](./assets/endpoints.png)
<p align="center" ><b>Figure 3</b>: <i>The endpoints that we are going to realize in this lesson.</i></p>

