# Introduction

Please read the general [introduction to the booking kata](../README.md) first!

# Getting started

First, create an intial Java kata set-up as described [here](https://github.com/zhendrikse/tdd/tree/master/cookiecutter).
We suggest to name your kata "Hotel" when prompted.

Next, you may want to go the the newly created project directory and consult
the provided ``README.md`` in there.

# The implementation

We start with the user story to create a booking. We could equally well have
started with the user story to view all bookings, of course.

## Making a booking

### Step 1: create our first booking

Let's create a first test. Since the hotel is empty, we may safely 
assume that every first booking succeeds.

How do we assert that booking has successfully been completed?
By verifying a `BookingCreatedEvent` has been "sent", of course!

However, since we don't have an event bus yet, we decide to store
all the change events in the aggregate root `Hotel` itself. Note
that this explains the word "aggregate", as the `Hotel` aggregates
all change events.

Obviously, it would be evil to just expose all these events to the
outside world. As in the (near) future we have to be able to store the
events in an event store (via a Repository), let's assume there will be
a method `persist()` in the `Hotel` aggregate, that returns an immutable
set of change events that need to be persisted.

```java
class HotelTest {
    private static final String BLUE_ROOM_NAME = "The Blue Room";
    private static final LocalDate AN_ARRIVAL_DATE = LocalDate.of(2020, 1, 20);
    private static final LocalDate A_DEPARTURE_DATE = LocalDate.of(2020, 1, 22);
    private static final UUID A_UUID = UUID.randomUUID();

    private final BookingCommand blueRoomBookingCommand = new BookingCommand(
        A_UUID, BLUE_ROOM_NAME, AN_ARRIVAL_DATE, A_DEPARTURE_DATE
      );

    @Test 
    void firstBookingCanAlwaysBeMade() {
        Hotel hotel = new Hotel(new ArrayList<Event>());
        hotel.onCommand(blueRoomBookingCommand);
      
        assertTrue(hotel.persist().size() == 1);
        assertTrue(hotel.persist().get(0) instanceof BookingCreatedEvent);

        BookingCreatedEvent event = (BookingCreatedEvent) hotel.persist().get(0);
        assertEquals(event.clientId, A_UUID);
        assertEquals(event.roomName, BLUE_ROOM_NAME);
        assertEquals(event.arrivalDate, AN_ARRIVAL_DATE);
        assertEquals(event.departureDate, A_DEPARTURE_DATE);
    }
}
``` 

Note that we already require the constructor of `Hotel` to receive a list
of events, so that the `Hotel` aggregate can be re-hydrated in the future. 
For now we will leave this list empty though.

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
    private final List<Event> changes;
  
    public Hotel(final List<Event> events) {
        this.changes = new ArrayList<Event>();
    }

    public void onCommand(final BookingCommand command) {
    }

    @Override
    public List<Event> persist() {
        return Collections.unmodifiableList(this.changes);
    }
}
```

where we introduced the `AggregateRoot` interface, as we eventually aim to
be able to persist all aggregate roots (not just the `Hotel` aggregate, of course).

```java
public interface AggregateRoot {
   List<Event> persist();
}
```

The test still fails though, as no events are created yet. So let's add a
`BookingCreatedEvent` to the list of event changes:

```java
    public void onCommand(final BookingCommand command) {
      BookingCreatedEvent event = new BookingCreatedEvent(
        command.clientId, command.roomName, command.arrivalDate, command.departureDate);
      this.changes.add(event);
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
        Hotel hotel = new Hotel(new ArrayList<Event>());
        hotel.onCommand(blueRoomBookingCommand);
        hotel.onCommand(blueRoomBookingCommand);
      
        assertTrue(hotel.persist().size() == 2);
        assertTrue(hotel.persist().get(1) instanceof BookingFailedEvent);

        BookingFailedEvent event = (BookingFailedEvent) hotel.persist().get(1);
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
    private final List<Event> changes;
    private final List<Booking> bookings = new ArrayList<>();
  
    public Hotel(final List<Event> events) {
        this.changes = new ArrayList<Event>();
    }

    private void bookingFails(final BookingCommand command) {
        BookingFailedEvent event = new BookingFailedEvent(
          command.clientId, command.roomName, command.arrivalDate, 
  command.departureDate);
        this.changes.add(event);
    }
  
    private void bookingSucceeds(final BookingCommand command) {
        BookingCreatedEvent event = new BookingCreatedEvent(
          command.clientId, command.roomName, command.arrivalDate, command.departureDate);
        this.changes.add(event);
        onEvent(event);
    }    
      
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

    @Override
    public List<Event> persist() {
        return Collections.unmodifiableList(this.changes);
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
- When the booking fails, we just append a `BookingFailedEvent` to the list of changes.
- When a booking succeeds, we delegate the creation of a new booking to a dedicated
  `onEvent(BookingCreatedEvent event)` method, as we want to be able to process this
  event also when rehydrating the aggregate root from the event store. In addition,
  this way the code nicely expresses intent.
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

    @BeforeEach
    void setUpHotelWithBlueRoomBooking() {
        this.hotel = new Hotel(new ArrayList<Event>());
        hotel.onCommand(blueRoomBookingCommand);
    }
```

### Step 3: make a booking at the same date but a different room

Let's introduce a red room in our tests:

```java
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
          A_UUID, BLUE_ROOM_NAME, AN_ARRIVAL_DATE.plusDays(4), A_DEPARTURE_DATE.plusDays(4)
        );
        hotel.onCommand(command);
      
        assertTrue(hotel.persist().size() == 2);
        assertTrue(hotel.persist().get(1) instanceof BookingCreatedEvent);

        BookingCreatedEvent event = (BookingCreatedEvent) hotel.persist().get(1);
        assertEquals(event.clientId, A_UUID);
        assertEquals(event.roomName, BLUE_ROOM_NAME);
        assertEquals(event.arrivalDate, AN_ARRIVAL_DATE.plusDays(4));
        assertEquals(event.departureDate, A_DEPARTURE_DATE.plusDays(4));
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
          A_UUID, BLUE_ROOM_NAME, AN_ARRIVAL_DATE.minusDays(4), A_DEPARTURE_DATE.minusDays(4)
        );
        hotel.onCommand(command);
      
        assertTrue(hotel.persist().size() == 2);
        assertTrue(hotel.persist().get(1) instanceof BookingCreatedEvent);

        BookingCreatedEvent event = (BookingCreatedEvent) hotel.persist().get(1);
        assertEquals(event.clientId, A_UUID);
        assertEquals(event.roomName, BLUE_ROOM_NAME);
        assertEquals(event.arrivalDate, AN_ARRIVAL_DATE.minusDays(4));
        assertEquals(event.departureDate, A_DEPARTURE_DATE.minusDays(4));
    }
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

We still lack a test for a reservation where the reservation periods are not 
identical but do (partially) overlap

```java
    @Test 
    void bookingTheSameRoomForOverlappingDatesShouldFail() {
        BookingCommand command = new BookingCommand(
          A_UUID, BLUE_ROOM_NAME, AN_ARRIVAL_DATE.plusDays(1), A_DEPARTURE_DATE.plusDays(1)
        );
        hotel.onCommand(command);
      
        assertTrue(hotel.persist().size() == 2);
        assertTrue(hotel.persist().get(1) instanceof BookingFailedEvent);

        BookingFailedEvent event = (BookingFailedEvent) hotel.persist().get(1);
        assertEquals(event.clientId, A_UUID);
        assertEquals(event.roomName, BLUE_ROOM_NAME);
        assertEquals(event.arrivalDate, AN_ARRIVAL_DATE.minusDays(1));
        assertEquals(event.departureDate, A_DEPARTURE_DATE.minusDays(1));
    }
``` 

which leads us to

```java
  private boolean canBookingBeMade(final Booking requestedBooking, final Booking existingBooking) {
      if (!existingBooking.roomName.equals(requestedBooking.roomName)) 
          return true;

      if (requestedBooking.arrivalDate.compareTo(existingBooking.arrivalDate) >= 0 &&
          requestedBooking.arrivalDate.compareTo(existingBooking.departureDate) <=0)
          return false;
  
      return true;
  }

  private boolean canBookingBeMade(final Booking requestedBooking) {
    for (final Booking existingBooking : this.bookings) {
      if (!canBookingBeMade(requestedBooking, existingBooking))
        return false;
    }
    
    return true;
  }
  
  public void onCommand(final BookingCommand command) {
      final Booking requestedBooking = new Booking(
        command.clientId, command.roomName, command.arrivalDate, command.departureDate);
      if (canBookingBeMade(requestedBooking))
        bookingSucceeds(command);
      else
        bookingFails(command);
  }
  ```

Finally, let's get rid of the [feature envy]() in the comparison of booking dates 
by moving the decision logic into the `Booking` class:

```java
  private boolean canBookingBeMade(final Booking requestedBooking, final Booking existingBooking) {
      if (!existingBooking.roomName.equals(requestedBooking.roomName)) 
          return true;

      if (existingBooking.isDateBetweenArrivalAndDepartureDates(requestedBooking.arrivalDate))
          return false;
  
      return true;
  }
  
  // ...

    class Booking implements Event {

      // ...
      
      public boolean isDateBetweenArrivalAndDepartureDates(final LocalDate aDate) {
          return aDate.compareTo(this.arrivalDate) >= 0 && aDate.compareTo(this.departureDate) <=0;
      }

```




## Overview of the reservations