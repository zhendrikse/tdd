# Introduction

Please read the general [introduction to the booking kata](../README.md) first!

# Getting started

First, create an initial Java kata set-up as described [here](https://github.com/zhendrikse/tdd/tree/master/cookiecutter).
We suggest naming your kata "Hotel" when prompted.

Next, you may want to go to the newly created project directory and consult
the provided ``README.md`` in there.

# The implementation

We start with the user story to create a booking. 

## Making a booking

### Step 1: create our first booking

Let's create a first test. Since the hotel is empty, we may safely 
assume that every first booking succeeds.

How do we assert that the booking has successfully been completed?
By verifying a `BookingCreatedEvent` has been "sent", of course!
We have put the word sent between quotes since we don't have 
an event bus yet. So what can we do instead?

The first step toward a possible approach is to realize that 
all the events created by the aggregate root `Hotel` need to 
be collected somehow somewhere. By the way, note that this also
explains the word "aggregate", as the `Hotel` aggregates
all change events.

Events emitted by the `Hotel` aggregate are typically stored in
a database that is usually coined accordingly: the event store.

As this database is external to our domain (model), 
this in turn calls for yet another application of 
[ports &amp; adapters](https://alistair.cockburn.us/hexagonal-architecture/):
we are going to ask an event source repository to load and store the
events emitted by the `Hotel` aggregate. Formulated more precisely,
we ask the repository to load and store the `Hotel` aggregate itself, 
as its state is uniquely determined (rehydrated) by 
the events stored in the event store (using the `apply()` method).

We can already make use of this fact, by plugging in a stub event
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
be able to persist more hotels than one particular hotel only.

```java
public interface AggregateRoot {
   UUID getId();
}
```

Any realistic implementation of the repository interface characterizing
the event store will eventually use this `getId()` method.

```java
public interface EventSourceRepository<Hotel> {
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

    class Booking {
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

Let's analyze this code in a bit more detail:

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
- Notice that we never use parenthesis in `if`-statements. As soon as we need multiple
  statements in an `if`-statement, we write a (private) method that explains what we
  want to achieve.

Let's finally clean up the duplication in the tests by applying the DRY principle,
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

### Step 3: make a booking on the same date but for a different room

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

### Step 4: booking an identical room on an available date

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
    return this.bookings
      .stream()
      .filter(booking -> booking.doesConflictWith(requestedBooking))
      .collect(toList())
      .isEmpty();  
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

Also, we need to implement the `apply()` method of the aggregate in both
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
`instanceof` checks? Yes, we can!

```java
  @Override
  public void apply(final Event event) {
    this.onEventDispatcher.get(event.getClass()).accept(event);
  }
``` 

where

```java
public class Hotel implements AggregateRoot {
    // ...
  
    private final Map<Class, Consumer<Event>> onEventDispatcher = new HashMap<>();

    public Hotel(final EventSourceRepository repository) {
        this.eventSourceRepository = repository;
        initOnEventDispatcherMap();
    }

    private void initOnEventDispatcherMap() {
        this.onEventDispatcher.put(BookingCreatedEvent.class, event -> onEvent((BookingCreatedEvent) event));
        this.onEventDispatcher.put(BookingFailedEvent.class, event -> onEvent((BookingFailedEvent) event));
    }
```

## Implementation of the event store

### Introduction

According to [Implementing Event Sourcing in Python – part 2, robust event store atop PostgreSQL](https://breadcrumbscollector.tech/implementing-event-sourcing-in-python-part-2-robust-event-store-atop-postgresql/),
an event store should accommodate all types of events by storing them as follows:

```
Events
---------------------------------------
| uuid | aggregate_uuid | name | data |
---------------------------------------
```

To retrieve a stream of events from the event store (see
[Returning Stream vs. Collection](https://www.baeldung.com/java-return-stream-collection)), 
let's extend the `EventStoreRepository` interface accordingly

```java
public interface EventSourceRepository<Hotel> {
  void save(UUID aggregateRootId, Event newEvent);
  
  Hotel load(UUID aggregateRootId);
  
  Stream<Event> loadStream(UUID aggregateRootId);
}
```

### In-memory event store

In order to be able to connect our projections to the event store, we need
a minimalistic implementation of the `EventStoreRepository` interface.
Obviously, we are going to do that in a test-driven development manner as well!

Our first test could very well look like this:

```java
class CsvEventSourceRepositoryTest {
    @Test
    void repositoryContainsBookingCreatedEventAfterSuccessfulBookings() {
        EventSourceRepository repository = new InMemoryEventSourceRepository();
        Hotel hotel = new Hotel(repository);
        hotel.onCommand(HotelTest.BLUE_ROOM_BOOKING_COMMAND);
        hotel.onCommand(HotelTest.RED_ROOM_BOOKING_COMMAND);
        
        Stream eventStream = repository.loadStream(hotel.getId());
        assertEquals(eventStream.count(), 2);
    }
}
```

where we have made both the `HotelTest` class as well as the booking commands
in their public (and the latter also final static, of course);

A minimal implementation would thus become

```java
public class InMemoryEventSourceRepository implements EventSourceRepository<Hotel> {
  private final List<Event> eventStore = new ArrayList<>();

  @Override
  public void save(final UUID aggregateRootId, final Event newEvent) {
      this.eventStore.add(newEvent);
  }
  
  @Override
  public Hotel load(final UUID aggregateRootId) {
    return null;
  }

  @Override
  public Stream<Event> loadStream(final UUID aggregateRootId) {
    return eventStore.stream();
  }
}
```

If we insist on being able to support different aggregate roots in our
in-memory event store, we have to force a per-aggregate ID:

```java
    @Test
    void repositoryDistinguishesBetweenDifferentAggregateRoots() {
        EventSourceRepository repository = new InMemoryEventSourceRepository();
        
        Hotel hotel1 = new Hotel(repository);
        hotel1.onCommand(HotelTest.BLUE_ROOM_BOOKING_COMMAND);
        Hotel hotel2 = new Hotel(repository);
        hotel2.onCommand(HotelTest.RED_ROOM_BOOKING_COMMAND);
        
        Stream eventStream = repository.loadStream(hotel1.getId());
        assertEquals(eventStream.count(), 1);
    }
```

Of course, this test immediately fails, so we have to generalize our
implementation like so

```java
  private final Map<UUID, List<Event>> eventStore = new HashMap<>();

  @Override
  public void save(final UUID aggregateRootId, final Event newEvent) {
      if (!eventStore.containsKey(aggregateRootId))
        eventStore.put(aggregateRootId, new ArrayList<>());

      this.eventStore.get(aggregateRootId).add(newEvent);
  }
  
  @Override
  public Hotel load(final UUID aggregateRootId) {
    return null;
  }

  @Override
  public Stream<Event> loadStream(final UUID aggregateRootId) {
    return eventStore.get(aggregateRootId).stream();
  }
```

This implementation will suffice for testing our projections.

## Overview of the reservations

### Towards a query model: a list with bookings

Let's create a test that verifies our list with bookings after
one (or optionally more) booking(s) have been made.

```java
class BookingEventHandlerTest {
    @Test
    void createsListWithBookingsFromBookingsEventStream() {
        List<Event> eventList = new ArrayList<>();
        eventList.add(new BookingCreatedEvent(UUID.randomUUID(), "room one", LocalDate.of(2001, 1, 1), LocalDate.of(2001, 1, 11)));
        Stream<Event> eventStream = eventList.stream();

        final EventHandler bookingEventHandler = new BookingEventHandler();
        eventStream.forEach(bookingEventHandler::onEvent);
        assertEquals(((BookingEventHandler) bookingEventHandler).getBookings().size(), 1);
    }
}
```

We mock the stream of events that we eventually are going to get from the event repository.
We apply the `onEvent(Event)` method from the event handler to each event:

```java
public class BookingEventHandler implements EventHandler {
    private final List<Booking> bookings = new ArrayList<>();

    @Override
    public void onEvent(final Event event) {
        if (event instanceof BookingCreatedEvent) {
            BookingCreatedEvent bookingEvent = (BookingCreatedEvent) event;
            bookings.add(new Booking(bookingEvent.clientId, bookingEvent.roomName, bookingEvent.arrivalDate, bookingEvent.departureDate));
        }
    }

    public List<Booking> getBookings() {
        return Collections.unmodifiableList(bookings);
    }
}
```

We notice that the `Booking` class is actually a value object, that we need on both
the command and query sides of the application, hence we promote this class from
within `Hotel` to its own file.

This makes our test pass. At the same time, we recognize something we have seen before.
The `BookingEventHandler` is in need of the same event dispatcher that we implemented in 
the `Hotel` class! So let's apply the DRY principle and share this code.

After a series of small steps, we eventually arrive at a dedicated event dispatcher:

```java
public class EventDispatcher {
    private final Map<Class, Consumer<Event>> onEventDispatcher = new HashMap<>();
    private final EventHandler eventHandler;

    public EventDispatcher(final EventHandler eventHandler) {
        initOnEventDispatcherMap();
        this.eventHandler = eventHandler;
    }

    private void initOnEventDispatcherMap() {
        onEventDispatcher.put(BookingCreatedEvent.class, event -> eventHandler.onEvent((BookingCreatedEvent) event));
        onEventDispatcher.put(BookingFailedEvent.class, event -> eventHandler.onEvent((BookingFailedEvent) event));
    }

    public void dispatch(final Event event) {
        onEventDispatcher.get(event.getClass()).accept(event);
    }
}
```

The event handler interface is defined as

```java
public interface EventHandler {
    void onEvent(BookingFailedEvent event);

    void onEvent(BookingCreatedEvent event);

    void onEvent(Event event);
}
```

Both the aggregate root and query-side event handlers should implement this interface.
For the aggregate root interface, we opted to rename the `apply(Event)` method to
`onEvent(Event)`. We could equally well have chosen for naming the `onEvent(Event)`
method in the `EventHandler` interface `apply(Event)`.

The booking event handler now becomes

```java
public class BookingEventHandler implements EventHandler {
    private final List<Booking> bookings = new ArrayList<>();
    private final EventDispatcher eventDispatcher = new EventDispatcher(this);

    @Override
    public void onEvent(final BookingCreatedEvent event) {
        BookingCreatedEvent bookingEvent = (BookingCreatedEvent) event;
        bookings.add(new Booking(bookingEvent.clientId, bookingEvent.roomName, bookingEvent.arrivalDate, bookingEvent.departureDate));
    }

    @Override 
    public void onEvent(final BookingFailedEvent event) {}

    @Override
    public void onEvent(final Event event) {
        eventDispatcher.dispatch(event);
    }

    public List<Booking> getBookings() {
        return Collections.unmodifiableList(bookings);
    }
}
```

Analogously we can do the same in the `Hotel` class, that now should implement
the `EventHandler` interface via the `AggregateRoot` interface as well.

```java
public interface AggregateRoot extends EventHandler {
   UUID getId();
}
```

## Implementing the query

Are we now ready to implement the required query 
`Room[] freeRooms(arrival: Date, departure: Date)`?

Note that the question is to list those rooms that are _not_ 
booked. So we should somehow have a notion of all available rooms in
our hotel. 

The simplest thing that could possibly work is to add a fixed number 
of predefined rooms to our hotel. Obviously, this is going to be a 
fatal limitation once we want to support multiple different hotels.

Assuming we have to support just one hotel yet, we introduce an 
enumeration of rooms in our hotel and refactor the stringly typed 
([primitive obsession](https://refactoring.guru/smells/primitive-obsession)) 
room parameters.

```java
public enum Room {
  BLUE_ROOM("Blue room"),
  RED_ROOM("Red room"),
  GREEN_ROOM("Green room"),
  YELLOW_ROOM("Yellow room"),
  BROWN_ROOM("Brown room");

  private String name;
 
  Room(final String name) {
      this.name = name;
  }

  @Override
  public String toString() {
      return name;
  }
}
```

Finally, we can write a test that ties everything together. Our approach will be:
- Tie everything together, i.e. implement the 
  [BASE](https://www.techopedia.com/definition/29164/basically-available-soft-state-eventual-consistency-base)
  principle by requesting the event stream from the event store every time
  we issue our query.
- We set up a test where two rooms are booked on the dates that we will query on,
  hence we should end up with a list containing the other three free rooms.
- The event handler just builds up a list with all reservations. Later on, this
  may further be optimized to skip reservations in the past, as those aren't
  relevant to our query. Alternatively, we may want to keep those as well, as
  future/additional queries may need these old reservation data too.

```java
class RoomsQueryHandlerTest {

    @Test
    void listOfFreeRoomsForGivenTimePeriod() {
        EventSourceRepository repository = new InMemoryEventSourceRepository();
        Hotel hotel = new Hotel(repository);
        hotel.onCommand(HotelTest.BLUE_ROOM_BOOKING_COMMAND);
        hotel.onCommand(HotelTest.RED_ROOM_BOOKING_COMMAND);

        RoomsQueryHandler queryHandler = new RoomsQueryHandler(repository);
        AvailableRoomsQuery query = new AvailableRoomsQuery(
          hotel.getId(), HotelTest.AN_ARRIVAL_DATE, HotelTest.A_DEPARTURE_DATE);
        List<Room> availableRooms = queryHandler.onQuery(query);
        
        assertEquals(availableRooms.size(), 3);
        assertAll("Available rooms",
            () -> assertEquals("Green room", availableRooms.get(0).toString()),
            () -> assertEquals("Yellow room", availableRooms.get(1).toString()),
            () -> assertEquals("Brown room", availableRooms.get(2).toString())
        );
    }
}
```

We can make this test pass by hardcoding this list:

```java
public class RoomsQueryHandler {
  private final EventSourceRepository eventRepository;

  public RoomsQueryHandler(final EventSourceRepository eventRepository) {
    this.eventRepository = eventRepository;
  }

  public List<Room> onQuery(final AvailableRoomsQuery query) {
    final List<Room> availableRooms = new java.util.ArrayList<Room>();
    availableRooms.add(Room.GREEN_ROOM);
    availableRooms.add(Room.YELLOW_ROOM);
    availableRooms.add(Room.BROWN_ROOM);
    return availableRooms;
  }
}
```

with an available rooms query 

```java
public class AvailableRoomsQuery {
  public final LocalDate arrivalDate;
  public final LocalDate departureDate;
  public final UUID hotelId;
  
  public AvailableRoomsQuery(final UUID hotelId, final LocalDate arrivalDate, final LocalDate departureDate) {
    this.arrivalDate = arrivalDate;
    this.departureDate = departureDate;
    this.hotelId = hotelId;
  }
}
```

This hard-coded list can then be generalized to

```java
public class RoomsQueryHandler {
  private final EventSourceRepository eventRepository;
  private List<Booking> allBookings = new ArrayList<>();

  public RoomsQueryHandler(final EventSourceRepository eventRepository) {
    this.eventRepository = eventRepository;
  }

  private void updateListWithAllBookings(final UUID hotelId) {
    final BookingEventHandler bookingEventHandler = new BookingEventHandler();            
    final Stream<Event> eventStream = eventRepository.loadStream(hotelId);
    eventStream.forEach(bookingEventHandler::onEvent);
    allBookings = bookingEventHandler.getBookings();    
  }

  private boolean roomAvailable(final Booking queryBooking) {
      return allBookings
        .stream()
        .filter(queryBooking::doesConflictWith)
        .collect(toList())
        .isEmpty();
  }

  private List<Room> filterAvailableRoomsFromAllRooms(final AvailableRoomsQuery query) {
    updateListWithAllBookings(query.hotelId);
    return Stream
      .of(Room.values())
      .filter(room -> roomAvailable(
        new Booking(UUID.randomUUID(), room, query.arrivalDate, query.departureDate)))
      .collect(toList());
  }

  public List<Room> onQuery(final AvailableRoomsQuery query) {
    return filterAvailableRoomsFromAllRooms(query);
  }
}
```

## Further steps

We can further extend this code by:

- Adding a command to cancel a booked room
- Introducing a command bus
- Introducing an event bus
- Adding a REST endpoint
- Etc. 

