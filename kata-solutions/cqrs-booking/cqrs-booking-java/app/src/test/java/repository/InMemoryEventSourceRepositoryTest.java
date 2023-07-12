package repository;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.BeforeEach;
import java.util.UUID;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Stream;
import java.time.LocalDate;

import command.BookingCommand;
import hotel.Hotel;
import hotel.HotelTest;

class InMemoryEventSourceRepositoryTest {

    @Test
    void repositoryContainsBookingCreatedEventAfterSuccessfulBookings() {
        EventSourceRepository repository = new InMemoryEventSourceRepository();
        Hotel hotel = new Hotel(repository);
        hotel.onCommand(HotelTest.BLUE_ROOM_BOOKING_COMMAND);
        hotel.onCommand(HotelTest.RED_ROOM_BOOKING_COMMAND);
        
        Stream eventStream = repository.loadStream(hotel.getId());
        assertEquals(eventStream.count(), 2);
    }

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
}