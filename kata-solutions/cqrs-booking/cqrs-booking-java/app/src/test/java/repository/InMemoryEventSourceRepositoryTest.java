package repository;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.stream.Stream;

import org.junit.jupiter.api.Test;

import event.Event;
import hotel.Hotel;
import hotel.HotelTest;

class InMemoryEventSourceRepositoryTest {

    @Test
    void repositoryContainsBookingCreatedEventAfterSuccessfulBookings() {
        EventSourceRepository<Hotel> repository = new InMemoryEventSourceRepository();
        Hotel hotel = new Hotel(repository);
        hotel.onCommand(HotelTest.BLUE_ROOM_BOOKING_COMMAND);
        hotel.onCommand(HotelTest.RED_ROOM_BOOKING_COMMAND);

        Stream<Event> eventStream = repository.loadStream(hotel.getId());
        assertEquals(eventStream.count(), 2);
    }

    @Test
    void repositoryDistinguishesBetweenDifferentAggregateRoots() {
        EventSourceRepository<Hotel> repository = new InMemoryEventSourceRepository();

        Hotel hotel1 = new Hotel(repository);
        hotel1.onCommand(HotelTest.BLUE_ROOM_BOOKING_COMMAND);
        Hotel hotel2 = new Hotel(repository);
        hotel2.onCommand(HotelTest.RED_ROOM_BOOKING_COMMAND);

        Stream<Event> eventStream = repository.loadStream(hotel1.getId());
        assertEquals(eventStream.count(), 1);
    }
}