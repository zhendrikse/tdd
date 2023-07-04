# Introduction

This kata is based on the [CQRS Booking kata](https://codingdojo.org/kata/CQRS_Booking/).
The aim is to write a simple booking soluiton using 
the [CQRS architectural pattern](https://martinfowler.com/bliki/CQRS.html).

## Features

The aim is to be able to create a booking solution for one hotel.

The first 2 users stories are:

- As a user I whant to see all free rooms.
- As a user I whant to book a room.

As stated in the introduction, the constraint is that we have to use the CQRS pattern

To do that we will have :

- One create-booking command.
  
  The booking command contains the following fields:
  ``` 
  client id
  room name
  arrival date
  departure date
  ```

- One view-bookings query: 
  `Room[] freeRooms(arrival: Date, departure: Date)`. 

  The room value object contains one field only:
  ```
  room name
  ```

  ## Considerations and decisions

  - Start out without event sourcing
  - Optionally add event sourcing
  