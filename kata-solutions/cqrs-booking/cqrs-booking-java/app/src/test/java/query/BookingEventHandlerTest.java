package query;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.BeforeEach;

import java.time.LocalDate;
import java.util.UUID;
import java.util.ArrayList;
import java.util.List;
import java.util.UUID;
import java.util.stream.Stream;
import java.time.LocalDate;

import event.BookingCreatedEvent;
import event.Event;
import hotel.Booking;
import query.eventhandler.EventHandler;
import query.eventhandler.BookingEventHandler;

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