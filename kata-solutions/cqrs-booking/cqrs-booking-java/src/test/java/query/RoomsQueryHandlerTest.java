package query;

import static org.junit.jupiter.api.Assertions.assertAll;
import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.List;

import org.junit.jupiter.api.Test;

import hotel.Hotel;
import hotel.HotelTest;
import hotel.Room;
import repository.EventSourceRepository;
import repository.InMemoryEventSourceRepository;

class RoomsQueryHandlerTest {

    @Test
    void listOfFreeRoomsForGivenTimePeriod() {
        EventSourceRepository<Hotel> repository = new InMemoryEventSourceRepository();
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
                () -> assertEquals("Brown room", availableRooms.get(2).toString()));
    }
}