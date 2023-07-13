package query;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.BeforeEach;

import java.util.List;

import query.AvailableRoomsQuery;
import query.RoomsQueryHandler;
import hotel.Room;
import hotel.HotelTest;
import hotel.Hotel;
import repository.InMemoryEventSourceRepository;
import repository.EventSourceRepository;

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