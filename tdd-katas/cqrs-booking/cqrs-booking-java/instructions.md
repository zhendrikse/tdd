# Introduction

Please read the general [introduction to the booking kata](../README.md) first!

# Getting started

First, create an intial Java kata set-up as described [here](https://github.com/zhendrikse/tdd/tree/master/cookiecutter).
We suggest to name your kata "Hotel" when prompted.

Next, you may want to go the the newly created project directory and consult
the provided ``README.md`` in there.

# The implementation

We start with the user story to create a booking. 

## Making a booking

### Step 1: create our first booking

Let's create a first test. Since the hotel is empty, we may safely 
assume that every first booking succeeds.

How do we assert that booking has successfully been completed?
By verifying a `BookingCreatedEvent` has been "sent", of course!
We have put the word sent between quotes, since we don't have 
an event bus yet. So what can we do instead?

A first step towards a possible approach is to realize that 
all the change emitted created by the aggregate root `Hotel` need to 
be collected somehow shomewhere. By the way, note that this also
explains the word "aggregate", as the `Hotel` aggregates
all change events.

Events emitted by the `Hotel` aggregate are typically stored in
a database that is usually coined accordingly: the event store.

As this database is external to our domain (model), 
this in turn calls for yet another application of ports &amp; adapters:
we are going to ask an event source repository to load and store the
events emitted by the `Hotel` aggregate. Formulated more precisely,
we ask the repository to load and store the `Hotel` aggregate itself, 
as its state is uniquely determined (rehydrated) by 
the events stored in the event store (using the `apply()` method).

We can already make use of this fact, by pluggin in a stub event
source repository for now. We can query this stub repository 
for the events that have (or haven't) been sent! 
So let's start with a stub event source
repository right from the start and use in our tests.

```java
class HotelTest {
    private static final String BLUE_ROOM_NAME = "The Blue Room";
    private static final LocalDate AN_ARRIVAL_DATE = LocalDate.of(2020, 1, 20);
    private static final LocalDate A_DEPARTURE_DATE = LocalDate.of(2020, 1, 22);
    private static final UUID A_CLIENT_UUID = UUID.randomUUID();

    private final BookingCommand blueRoomBookingCommand = new BookingCommand(
        A_CLIENT_UUID, BLUE_ROOM_NAME, AN_ARRIVAL_DATE, A_DEPARTURE_DATE
      );

    @Test 
    void firstBookingCanAlwaysBeMade() {
        StubEventSourceRepository repository = new StubEventSourceRepository();
        Hotel hotel = new Hotel(repository);
        hotel.onCommand(blueRoomBookingCommand);

        List<Event> events = repository.getEventsFor(hotel.getId());
        assertTrue(events.size() == 1);
        assertTrue(events.get(0) instanceof BookingCreatedEvent);

        BookingCreatedEvent event = (BookingCreatedEvent) events.get(0);
        assertEquals(event.clientId, A_UUID);
        assertEquals(event.roomName, BLUE_ROOM_NAME);
        assertEquals(event.arrivalDate, AN_ARRIVAL_DATE);
        assertEquals(event.departureDate, A_DEPARTURE_DATE);
    }
}
``` 

Note that we already require the constructor of `Hotel` to receive a reference
to the event store repository, so that we can query the events stored in that repository
after the command has been handled. 

So let's first define the `BookingCommand`:

```java
public class BookingCommand {
    public final UUID clientId; 
    public final String roomName;
    public final LocalDate arrivalDate;
    public final LocalDate departureDate;
    
    public BookingCommand(final UUID clientId, final String roomName, final LocalDate arrivalDate, final LocalDate departureDate) {
        this.clientId = clientId;
        this.roomName = roomName;
        this.arrivalDate = arrivalDate;
        this.departureDate = departureDate;
    }

    @Override
    public String toString() { 
      return "clientId: '" + this.clientId + "', roomName: '" + this.roomName + "', arrivalDate: '" + this.arrivalDate + "', departureDate: '" + this.departureDate + "'";
    } 
}
``` 

and likewise a `BookingCreatedEvent`. 

```java
public class BookingCreatedEvent implements Event {
    public final UUID clientId; 
    public final String roomName;
    public final LocalDate arrivalDate;
    public final LocalDate departureDate;
    
    public BookingCreatedEvent(final UUID clientId, final String roomName, final LocalDate arrivalDate, final LocalDate departureDate) {
        this.clientId = clientId;
        this.roomName = roomName;
        this.arrivalDate = arrivalDate;
        this.departureDate = departureDate;
    }

    @Override
    public String toString() { 
      return "clientId: '" + this.clientId + "', roomName: '" + this.roomName + "', arrivalDate: '" + this.arrivalDate + "', departureDate: '" + this.departureDate + "'";
    } 
}
```

Since we want to be able to store all events
in a list, we'll provide an `Event` tagging interface as well.

```java
public interface Event {}
```

Let's finally implement the most minimalistic version of the `Hotel` aggregate root
that makes the compilation succeed:

```java
public class Hotel implements AggregateRoot {
    private final UUID id = UUID.randomUUID();
    private final EventSourceRepository eventSourceRepository;

    public Hotel(final EventSourceRepository repository) {
        this.eventSourceRepository = repository;
    }

    @Override 
    public UUID getId() {
        return id;
   }

    public void onCommand(final BookingCommand command) {
    }
}
```

where we introduced the `AggregateRoot` interface, as we eventually aim to
be able to persist more than one particular hotel.

```java
public interface AggregateRoot {
   UUID getId();
}
```

Any realistic implementation of the repository interface characterizing
the event store will eventually use this `getId()` method.

```java
ublic interface EventSourceRepository<Hotel> {
  void save(UUID aggregateRootId, Event event);
}
```

together with its implementation

```java
public class StubEventSourceRepository implements EventSourceRepository {
  private final List<Event> eventList;

  public StubEventSourceRepository() {
    this.eventList = new ArrayList<Event>();
  }

  @Override
  public void save(final UUID aggregateRootId, final Event event) {
    this.eventList.add(event);
  }
  
  public List<Event> getEventsFor(final UUID aggregateRootId) {
      return Collections.unmodifiableList(this.eventList);
  }
}
```

The test still fails though, as no events are created yet. So let's add a
`BookingCreatedEvent` to the list of event changes:

```java
    public void onCommand(final BookingCommand command) {
      BookingCreatedEvent event = new BookingCreatedEvent(
        command.clientId, command.roomName, command.arrivalDate, command.departureDate);
      this.eventSourceRepository.save(this.id, event);
    }
```

And voila, we have our first passing test!

### Step 2: create the same booking twice

When we try to make the same reservation a second time, this should result in a
`BookingFailedEvent`:

```java
public class BookingFailedEvent implements Event {
    public final UUID clientId; 
    public final String roomName;
    public final LocalDate arrivalDate;
    public final LocalDate departureDate;
    
    public BookingFailedEvent(final UUID clientId, final String roomName, final LocalDate arrivalDate, final LocalDate departureDate) {
        this.clientId = clientId;
        this.roomName = roomName;
        this.arrivalDate = arrivalDate;
        this.departureDate = departureDate;
    }

    @Override
    public String toString() { 
      return "clientId: '" + this.clientId + "', roomName: '" + this.roomName + "', arrivalDate: '" + this.arrivalDate + "', departureDate: '" + this.departureDate + "'";
    } 
}
```

So let's write a test for that scenario as well (where the second booking should lead to
a second booking-failed event):

```java
    @Test 
    void bookingTheSameRoomForTheSameDateShouldFail() {
        StubEventSourceRepository repository = new StubEventSourceRepository();
        Hotel hotel = new Hotel(repository);
        hotel.onCommand(blueRoomBookingCommand);
        hotel.onCommand(blueRoomBookingCommand);

        List<Event> events = repository.getEventsFor(hotel.getId());
        assertTrue(events.size() == 2);
        assertTrue(events.get(1) instanceof BookingFailedEvent);

        BookingFailedEvent event = (BookingFailedEvent) events.get(1);
        assertEquals(event.clientId, A_UUID);
        assertEquals(event.roomName, BLUE_ROOM_NAME);
        assertEquals(event.arrivalDate, AN_ARRIVAL_DATE);
        assertEquals(event.departureDate, A_DEPARTURE_DATE);
    }

```

The most simple solution is to maintain a list of bookings in the hotel, and
as soon as there is one booking already, we just bluntly refuse any other 
reservation:

```java
public class Hotel implements AggregateRoot {
    private final UUID id = UUID.randomUUID();
    private final EventSourceRepository eventSourceRepository;
    private final List<Booking> bookings = new ArrayList<>();

    public Hotel(final EventSourceRepository repository) {
        this.eventSourceRepository = repository;
    }

    @Override 
    public UUID getId() {
        return id;
   }

   private void bookingFails(final BookingCommand command) {
        BookingFailedEvent event = new BookingFailedEvent(
          command.clientId, command.roomName, command.arrivalDate, 
  command.departureDate);
        onEvent(event);
        this.eventSourceRepository.save(this.id, event);
    }
  
    private void bookingSucceeds(final BookingCommand command) {
        BookingCreatedEvent event = new BookingCreatedEvent(
          command.clientId, command.roomName, command.arrivalDate, command.departureDate);
        onEvent(event);
        this.eventSourceRepository.save(this.id, event);
    }    
      
    private void onEvent(final BookingFailedEvent event) {}
      
    private void onEvent(final BookingCreatedEvent event) {
        this.bookings.add(new Booking(
          event.clientId, event.roomName, event.arrivalDate, event.departureDate));
    }
    
    public void onCommand(final BookingCommand command) {
      if (this.bookings.isEmpty())
        bookingSucceeds(command);
      else
        bookingFails(command);
    }

    class Booking implements Event {
        public final UUID clientId; 
        public final String roomName;
        public final LocalDate arrivalDate;
        public final LocalDate departureDate;
        
        public Booking(final UUID clientId, final String roomName, final LocalDate arrivalDate, final LocalDate departureDate) {
            this.clientId = clientId;
            this.roomName = roomName;
            this.arrivalDate = arrivalDate;
            this.departureDate = departureDate;
        }
    }
}

``` 

Let's analyse this code in a bit more detail:

- We have introduced an inner class `Booking`. We made it an inner class, as it belongs
  to the `Hotel` aggregate root.
- We maintain a list of bookings in the hotel. As explained, to make the test succeed,
  we can just refuse any additional booking.
- When a booking succeeds, we delegate the creation of a new booking to a dedicated
  `onEvent(BookingCreatedEvent event)` method, as we want to be able to process this
  event also when rehydrating the aggregate root from the event store. In addition,
  this way the code nicely expresses intent.
- When the booking fails, we just sent a `BookingFailedEvent` to the event store.
  The handling is delegated to a method that does nothing for now.
- Notice that we never use parenthesis in `if`-statements. A soon as we need multiple
  statements in an `if`-statement, we write a (private) method that explains what we
  want to achieve.

Let's finally clean-up the duplication in the tests by applying the DRY principle,
and hence using the `BeforeEach` construct to set up an initial hotel with one
booking

```java
class HotelTest {
    // ...
  
    private Hotel hotel;
    private StubEventSourceRepository repository = new StubEventSourceRepository();

    @BeforeEach
    void setUpHotelWithBlueRoomBooking() {
        this.hotel = new Hotel(repository);
        hotel.onCommand(blueRoomBookingCommand);
    }
  
```

In order to reduce the complexity of the two tests we currently have, we also
apply extract method for the verification of the event fields. 

```java
class HotelTest {
    // ...
    
    private void verifyBookingFailedEvent(final BookingFailedEvent event, final BookingCommand bookingCommand) {
        assertEquals(event.clientId, bookingCommand.clientId);
        assertEquals(event.roomName, bookingCommand.roomName);
        assertEquals(event.arrivalDate, bookingCommand.arrivalDate);
        assertEquals(event.departureDate, bookingCommand.departureDate);
    }

    private void verifyBookingCreatedEvent(final BookingCreatedEvent event, final BookingCommand bookingCommand) {
        assertEquals(event.clientId, bookingCommand.clientId);
        assertEquals(event.roomName, bookingCommand.roomName);
        assertEquals(event.arrivalDate, bookingCommand.arrivalDate);
        assertEquals(event.departureDate, bookingCommand.departureDate);
    }

    @Test 
    void firstBookingCanAlwaysBeMade() {
        List<Event> storedEvents = repository.getEventsFor(this.hotel.getId());
        assertTrue(storedEvents.size() == 1);
        assertTrue(storedEvents.get(0) instanceof BookingCreatedEvent);

        verifyBookingCreatedEvent((BookingCreatedEvent) storedEvents.get(0), blueRoomBookingCommand);
    }

    // ...
```

### Step 3: make a booking at the same date but a different room

Let's introduce a red room in our tests:

```java
    private static final String RED_ROOM_NAME = "The Red Room";
    
    // ...
    
    private final BookingCommand redRoomBookingCommand = new BookingCommand(
        A_UUID, RED_ROOM_NAME, AN_ARRIVAL_DATE, A_DEPARTURE_DATE
      );

    // ...
    
    @Test 
    void bookingDifferentRoomForTheSameDateShouldSucceed() {
        hotel.onCommand(redRoomBookingCommand);
      
        assertTrue(hotel.persist().size() == 2);
        assertTrue(hotel.persist().get(1) instanceof BookingCreatedEvent);

        BookingCreatedEvent event = (BookingCreatedEvent) hotel.persist().get(1);
        assertEquals(event.clientId, A_UUID);
        assertEquals(event.roomName, RED_ROOM_NAME);
        assertEquals(event.arrivalDate, AN_ARRIVAL_DATE);
        assertEquals(event.departureDate, A_DEPARTURE_DATE);
    }
```

We can make this test pass easily by modifying the `onCommand()` method slightly

```java
    public void onCommand(final BookingCommand command) {
      if (!this.bookings.isEmpty() && this.bookings.get(0).roomName.equals(command.roomName))
        bookingFails(command);
      else
        bookingSucceeds(command);
    }
```

Let's grab our refactor opportunity now to reorganize our classes a bit into packages,
by introducing separate folders for the aggregate root(s), commands, and events.

### Step 4: booking identical room on an available date

We are going to make the business logic a bit more explicit by demanding that
we can reserve the same room, as long as we reserve it on a different date!

```java
   @Test 
    void bookingIdenticalRoomForAvailableDateShouldSucceed() {
        BookingCommand command = new BookingCommand(
          A_CLIENT_UUID, BLUE_ROOM_NAME, AN_ARRIVAL_DATE.plusDays(4), A_DEPARTURE_DATE.plusDays(4)
        );
        hotel.onCommand(command);
      
        List<Event> storedEvents = repository.getEventsFor(this.hotel.getId());
        assertTrue(storedEvents.size() == 2);
        assertTrue(storedEvents.get(1) instanceof BookingCreatedEvent);

        verifyBookingCreatedEvent((BookingCreatedEvent) storedEvents.get(1), command);
    }
```

We now have to extend the business logic that approves the booking 

```java
  public void onCommand(final BookingCommand command) {
      if (bookingCanBeMade(command.roomName, command.arrivalDate, command.departureDate))
        bookingSucceeds(command);
      else
        bookingFails(command);
  }

  private boolean bookingCanBeMade(final String roomName, final LocalDate arrivalDate, final LocalDate departureDate) {
    if (this.bookings.isEmpty())
      return true;

    Booking existingBooking = this.bookings.get(0);
    if (!existingBooking.roomName.equals(roomName))
      return true;

    if (arrivalDate.isAfter(existingBooking.departureDate))
      return true;

    return false;
  }  
```

Likewise, if the departure date is before the arrival of the existing booking

```java
    @Test 
    void bookingIdenticalRoomWithDepartureBeforeArrivalOfExistingBookingShouldSucceed() {
        BookingCommand command = new BookingCommand(
          A_CLIENT_UUID, BLUE_ROOM_NAME, AN_ARRIVAL_DATE.minusDays(4), A_DEPARTURE_DATE.minusDays(4)
        );
        hotel.onCommand(command);
      
        List<Event> storedEvents = repository.getEventsFor(this.hotel.getId());
        assertTrue(storedEvents.size() == 2);
        assertTrue(storedEvents.get(1) instanceof BookingCreatedEvent);

        verifyBookingCreatedEvent((BookingCreatedEvent) storedEvents.get(1), command);
    }
```
We can make the test pass by adding yet another `if`-clause:

```java
    if (departureDate.isBefore(existingBooking.arrivalDate))
      return true;
``` 

These checks can easily be generalized for all bookings in the hotel:

```java
  private boolean bookingCanBeMade(final Booking requestedBooking, final Booking existingBooking) {
      if (!existingBooking.roomName.equals(requestedBooking.roomName) ||
          requestedBooking.arrivalDate.isAfter(existingBooking.departureDate) ||
          requestedBooking.departureDate.isBefore(existingBooking.arrivalDate))
        return true;
  
      return false;
  }

  private boolean bookingCanBeMade(final Booking requestedBooking) {
    for (final Booking existingBooking : this.bookings) {
      if (!bookingCanBeMade(requestedBooking, existingBooking))
        return false;
    }
    
    return true;
  }
  
  public void onCommand(final BookingCommand command) {
      final Booking requestedBooking = new Booking(
        command.clientId, command.roomName, command.arrivalDate, command.departureDate);
      if (bookingCanBeMade(requestedBooking))
        bookingSucceeds(command);
      else
        bookingFails(command);
  }
```

### Step 5: overlapping dates

We may think we still lack a test for a reservation where the reservation periods are not 
identical but do (partially) overlap

```java
    @Test 
    void bookingTheSameRoomForOverlappingArrivalDatesShouldFail() {
        BookingCommand command = new BookingCommand(
          A_CLIENT_UUID, BLUE_ROOM_NAME, AN_ARRIVAL_DATE.plusDays(1), A_DEPARTURE_DATE.plusDays(1)
        );
        hotel.onCommand(command);
      
        List<Event> storedEvents = repository.getEventsFor(this.hotel.getId());
        assertTrue(storedEvents.size() == 2);
        assertTrue(storedEvents.get(1) instanceof BookingFailedEvent);

        verifyBookingFailedEvent((BookingFailedEvent) storedEvents.get(1), command);
    }
``` 

However, this test jumps to green immediately, so our assumption is wrong. Whatever we
try, all cases are apparently covered already. What a pleasant surprise!

Finally, let's get rid of the [feature envy]() in the comparison of booking dates 
by moving the decision logic into the `Booking` class and playing a bit with the
boolean decision logic:

```java
  private boolean bookingCanBeMade(final Booking requestedBooking) {
    for (final Booking existingBooking : this.bookings) {
      if (existingBooking.doesConflictWith(requestedBooking))
        return false;
    }
    
    return true;
  }
  
  // ...

    class Booking implements Event {

      // ...
      
        public boolean doesConflictWith(final Booking anotherBooking) {
            return anotherBooking.roomName.equals(this.roomName) && 
              !(anotherBooking.arrivalDate.isAfter(this.departureDate) ||
              anotherBooking.departureDate.isBefore(this.arrivalDate));
        }
```

### Rehydrating the aggregate root by replaying all events

It is now time to see if we can resurrect a `Hotel` aggregate by replaying events.

```java
    @Test
    void rehydratedHotelAggregateShouldNotAllowDoubleReservations() {
        List<Event> events = new ArrayList<Event>();
        events.add(new BookingCreatedEvent(
            A_CLIENT_UUID, RED_ROOM_NAME, AN_ARRIVAL_DATE, A_DEPARTURE_DATE
        ));
        StubEventSourceRepository repository = new StubEventSourceRepository(events);
        Hotel rehydratedHotel = repository.load(UUID.randomUUID());
      
        rehydratedHotel.onCommand(redRoomBookingCommand);
      
        List<Event> storedEvents = repository.getEventsFor(rehydratedHotel.getId());
        assertTrue(storedEvents.size() == 2);
        assertTrue(storedEvents.get(1) instanceof BookingFailedEvent);

        verifyBookingFailedEvent((BookingFailedEvent) storedEvents.get(1), redRoomBookingCommand);
    }
  ```

Let's first extend the `EventSourceRepository`  and its stub implementation with
a `load()` operation

```java
 public StubEventSourceRepository() {
    this(new ArrayList<Event>());
  }
  
  public StubEventSourceRepository(final List<Event> events) {
      this.eventList = events;
  }

  @Override
  public Hotel load(final UUID aggregateRootId) {
      Hotel hotel = new Hotel(this);
      this.eventList.stream().forEach(event -> hotel.apply(event));
      return hotel;
  }

  // ...
``` 

Also, we need to implemet the `apply()` method of the aggregate in both
the `AggregateRoot` interface and `Hotel` aggregate:

```java  
  @Override
  public void apply(final Event event) {
    if (event instanceof BookingCreatedEvent) 
      onEvent((BookingCreatedEvent) event);
    else if (event instanceof BookingFailedEvent)
      onEvent((BookingFailedEvent) event);
  }
```

This makes our test pass.

Isn't there anything we can come up with to improve the conditionals based on the
`instanceof` checks?



## Overview of the reservations