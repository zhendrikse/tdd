package hotel;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.BeforeEach;
import java.util.UUID;
import java.util.ArrayList;
import java.util.List;
import java.time.LocalDate;

import command.BookingCommand;
import event.BookingCreatedEvent;
import event.BookingFailedEvent;
import event.Event;
import repository.StubEventSourceRepository;

public class HotelTest {
    private static final String BLUE_ROOM_NAME = "The Blue Room";
    private static final String RED_ROOM_NAME = "The Red Room";
    private static final LocalDate AN_ARRIVAL_DATE = LocalDate.of(2020, 1, 20);
    private static final LocalDate A_DEPARTURE_DATE = LocalDate.of(2020, 1, 22);
    private static final UUID A_CLIENT_UUID = UUID.randomUUID();

    public static final BookingCommand BLUE_ROOM_BOOKING_COMMAND = new BookingCommand(
        A_CLIENT_UUID, BLUE_ROOM_NAME, AN_ARRIVAL_DATE, A_DEPARTURE_DATE
      );
  
    public static final BookingCommand RED_ROOM_BOOKING_COMMAND = new BookingCommand(
        A_CLIENT_UUID, RED_ROOM_NAME, AN_ARRIVAL_DATE, A_DEPARTURE_DATE
      );
  
    private Hotel hotel;
    private StubEventSourceRepository repository = new StubEventSourceRepository();

    @BeforeEach
    void setUpHotelWithBlueRoomBooking() {
        this.hotel = new Hotel(repository);
        hotel.onCommand(BLUE_ROOM_BOOKING_COMMAND);
    }

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

        verifyBookingCreatedEvent((BookingCreatedEvent) storedEvents.get(0), BLUE_ROOM_BOOKING_COMMAND);
    }
  
    @Test 
    void bookingTheSameRoomForTheSameDateShouldFail() {
        hotel.onCommand(BLUE_ROOM_BOOKING_COMMAND);

        List<Event> storedEvents = repository.getEventsFor(this.hotel.getId());
        assertTrue(storedEvents.size() == 2);
        assertTrue(storedEvents.get(1) instanceof BookingFailedEvent);

        verifyBookingFailedEvent((BookingFailedEvent) storedEvents.get(1), BLUE_ROOM_BOOKING_COMMAND);
    }

    @Test 
    void bookingDifferentRoomForTheSameDateShouldSucceed() {
        hotel.onCommand(RED_ROOM_BOOKING_COMMAND);
      
        List<Event> storedEvents = repository.getEventsFor(this.hotel.getId());
        assertTrue(storedEvents.size() == 2);
        assertTrue(storedEvents.get(1) instanceof BookingCreatedEvent);

        verifyBookingCreatedEvent((BookingCreatedEvent) storedEvents.get(0), BLUE_ROOM_BOOKING_COMMAND);
    }

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
  
    @Test
    void rehydratedHotelAggregateShouldNotAllowDoubleReservations() {
        List<Event> events = new ArrayList<Event>();
        events.add(new BookingCreatedEvent(
            A_CLIENT_UUID, RED_ROOM_NAME, AN_ARRIVAL_DATE, A_DEPARTURE_DATE
        ));
        StubEventSourceRepository repository = new StubEventSourceRepository(events);
        Hotel rehydratedHotel = repository.load(UUID.randomUUID());
      
        rehydratedHotel.onCommand(RED_ROOM_BOOKING_COMMAND);
      
        List<Event> storedEvents = repository.getEventsFor(rehydratedHotel.getId());
        assertTrue(storedEvents.size() == 2);
        assertTrue(storedEvents.get(1) instanceof BookingFailedEvent);

        verifyBookingFailedEvent((BookingFailedEvent) storedEvents.get(1), RED_ROOM_BOOKING_COMMAND);
    }
}