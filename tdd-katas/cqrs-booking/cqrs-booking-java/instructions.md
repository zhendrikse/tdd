# Introduction

Please read the general [introduction to the booking kata](../README.md) first!

# Getting started

First, create an intial Java kata set-up as described [here](https://github.com/zhendrikse/tdd/tree/master/cookiecutter).
We suggest to name your kata "Hotel" when prompted.

Next, you may want to go the the newly created project directory and consult
the provided ``README.md`` in there.

# The implementation

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
        assertTrue(event.clientId == A_UUID);
        assertTrue(event.roomName == BLUE_ROOM_NAME);
        assertTrue(event.arrivalDate == AN_ARRIVAL_DATE);
        assertTrue(event.departureDate == A_DEPARTURE_DATE);
    }
}
``` 

So let's first define the `BookingCommand`:

```java
import java.util.UUID;
import java.time.LocalDate;

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

