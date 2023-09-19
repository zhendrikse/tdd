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
   $ cd BookingReferenceService
   $ dotnet run
   ```

2. Start the train data service by opening a terminal and type
   ```bash
   $ cd TrainDataService
   $ dotnet run
   ```

3. Start running the provided tests and scenario by opening a terminal and type
   ```bash
   $ ./run_tests.sh
   ```
   
Next, you can start coding the user story for the reservation of train tickets.

## Instructions to run the Booking Reference Service

You can get a unique booking reference using a REST-based service. 
The booking reference service fake is started using:

```bash
$ cd BookingReferenceService
$ dotnet run
```

The booking reference maybe obtained by posting a GET request to:

```bash
$ curl http://localhost:5041/booking_reference
```

This will return an hexadecimal booking reference like `75bcd15`.
   
## Instructions to run the Train Data Service

You can get a information on trains by using a dedicated REST-based service. 
This train data service stub is started using:

```bash
$ cd TrainDataService
$ dotnet run
``` 

### Retrieving train &amp; seat information 

You can use this service to get data for example about the train with ID 
`express_2000` like this:

```bash
$ curl http://localhost:5091/data_for_train/express_2000
```

this will return a json document with information about the seats that this train has:

```json
{"seats": {"1A": {"booking_reference": "", "seat_number": "1", "coach": "A"}, "2A": {"booking_reference": "", "seat_number": "2", "coach": "A"}}}
```

A seat is available if the "booking_reference" field contains an empty string. 

### Reserving seats on a train 

To reserve seats on a train, you'll need to make a POST request to this url:

```bash
$ curl http://localhost:5091/reserve
``` 

and attach form data for which seats to reserve. 

There should be three fields, namely `train_id`, `seats`, and `booking_reference`. 
The "seats" field should be a json encoded list of seat ids, for example `["1A", "2A"]`. 
The other two fields are ordinary strings. 
Note the server will prevent you from booking a seat that is already reserved with another booking reference.

### Freeing up all seats by removing all reservations 

The service has one additional method, that will remove all reservations on a particular train. Use it with care:

```bash
$ curl http://localhost:5091/reset/express_2000
```
