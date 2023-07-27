package query.eventhandler;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

import java.time.LocalDate;
import java.util.Arrays;
import java.util.List;
import java.util.UUID;

import org.junit.jupiter.api.Test;

import event.BookingCreatedEvent;
import event.Event;
import event.EventHandler;
import hotel.Room;

class BookingEventHandlerTest {
  private final EventHandler bookingEventHandler = new BookingEventHandler();

  @Test
  void createsListWithBookingsFromBookingsEventStream() {
    List<Event> eventList = Arrays.asList(
        new BookingCreatedEvent(
            UUID.randomUUID(), Room.BLUE_ROOM, LocalDate.of(2001, 1, 1), LocalDate.of(2001, 1, 11)));

    eventList.stream().forEach(bookingEventHandler::onEvent);
    assertEquals(((BookingEventHandler) bookingEventHandler).getBookings().size(), 1);
  }

  @Test
  void throwsAnUnimplementedErrorExceptionWhenDealingWithUnknownEvent() {
    UnsupportedOperationException thrown = assertThrows(UnsupportedOperationException.class, () -> {
      bookingEventHandler.onEvent(new Event() {
      });
    });
    assertEquals(thrown.getMessage(), "Event of type class query.eventhandler.BookingEventHandlerTest$1 not supported");
  }
}