# How to practice this kata

In this kata, you'll use two REST services during testing. 
These services act as test doubles, replacing their equivalent counterparts in production.
_The only difference will be the URLs that these services are invoked at_.

1. **A booking reference service**: 
   this service is used to obtain a unique booking reference.
2. **A train data service:**:
   this service is used to
   - assign a booking reference to one or more seats in a train
   - get an overview of all the seats in a train, where an empty booking reference
     field implies the seat is still available.

The latter will help you to set up certain scenarios for testing,
i.e. the "given" from the "given-when-then".

A rudimentary implementation of a ticket cancellation story has already 
been provided to get you up and running as quickly as possible.

# Getting started

## TLDR;

1. Start the booking reference service by opening a terminal and type
   ```bash
   $ cd booking_reference_service
   $ poetry install
   $ poetry run python -m booking_reference_service
   ```

2. Start the train data service by opening a terminal and type
   ```bash
   $ cd train_data_service
   $ poetry install
   $ poetry run python -m train_data_service_endpoint
   ```

3. Start running the provided tests and scenario by opening a terminal and type
   ```bash
   $ poetry run behave
   ```
   
Next, you can start coding the user story for the reservation of train tickets.