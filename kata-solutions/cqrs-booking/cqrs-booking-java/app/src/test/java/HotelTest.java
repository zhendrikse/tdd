import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.BeforeEach;
import java.util.UUID;
import java.util.ArrayList;
import java.time.LocalDate;

class HotelTest {
    private static final String BLUE_ROOM_NAME = "The Blue Room";
    private static final String RED_ROOM_NAME = "The Red Room";
    private static final LocalDate AN_ARRIVAL_DATE = LocalDate.of(2020, 1, 20);
    private static final LocalDate A_DEPARTURE_DATE = LocalDate.of(2020, 1, 22);
    private static final UUID A_UUID = UUID.randomUUID();

    private final BookingCommand blueRoomBookingCommand = new BookingCommand(
        A_UUID, BLUE_ROOM_NAME, AN_ARRIVAL_DATE, A_DEPARTURE_DATE
      );

    private final BookingCommand redRoomBookingCommand = new BookingCommand(
        A_UUID, RED_ROOM_NAME, AN_ARRIVAL_DATE, A_DEPARTURE_DATE
      );

    private Hotel hotel;

    @BeforeEach
    void setUpHotelWithBlueRoomBooking() {
        this.hotel = new Hotel(new ArrayList<Event>());
        hotel.onCommand(blueRoomBookingCommand);
    }

    @Test 
    void firstBookingCanAlwaysBeMade() {
        assertTrue(hotel.persist().size() == 1);
        assertTrue(hotel.persist().get(0) instanceof BookingCreatedEvent);

        BookingCreatedEvent event = (BookingCreatedEvent) hotel.persist().get(0);
        assertTrue(event.clientId == A_UUID);
        assertTrue(event.roomName == BLUE_ROOM_NAME);
        assertTrue(event.arrivalDate == AN_ARRIVAL_DATE);
        assertTrue(event.departureDate == A_DEPARTURE_DATE);
    }

    @Test 
    void sameBookingForSameRoomFails() {
        hotel.onCommand(blueRoomBookingCommand);
      
        assertTrue(hotel.persist().size() == 2);
        assertTrue(hotel.persist().get(1) instanceof BookingFailedEvent);

        BookingFailedEvent event = (BookingFailedEvent) hotel.persist().get(1);
        assertTrue(event.clientId == A_UUID);
        assertTrue(event.roomName == BLUE_ROOM_NAME);
        assertTrue(event.arrivalDate == AN_ARRIVAL_DATE);
        assertTrue(event.departureDate == A_DEPARTURE_DATE);
    }

    @Test 
    void sameBookingForDifferentRoomSucceeds() {
        hotel.onCommand(redRoomBookingCommand);
      
        assertTrue(hotel.persist().size() == 2);
        assertTrue(hotel.persist().get(1) instanceof BookingCreatedEvent);

        BookingCreatedEvent event = (BookingCreatedEvent) hotel.persist().get(1);
        assertTrue(event.clientId == A_UUID);
        assertTrue(event.roomName == RED_ROOM_NAME);
        assertTrue(event.arrivalDate == AN_ARRIVAL_DATE);
        assertTrue(event.departureDate == A_DEPARTURE_DATE);
    }
}
