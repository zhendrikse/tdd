package query.eventhandler;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import event.BookingCreatedEvent;
import event.BookingFailedEvent;
import event.Event;
import event.EventDispatcher;
import event.EventHandler;
import hotel.Booking;

public class BookingEventHandler implements EventHandler {
    private final List<Booking> bookings = new ArrayList<>();
    private final EventDispatcher eventDispatcher = new EventDispatcher(this);

    @Override
    public void onEvent(final BookingCreatedEvent event) {
        BookingCreatedEvent bookingEvent = (BookingCreatedEvent) event;
        bookings.add(new Booking(bookingEvent.clientId, bookingEvent.room, bookingEvent.arrivalDate,
                bookingEvent.departureDate));
    }

    @Override
    public void onEvent(final BookingFailedEvent event) {
    }

    @Override
    public void onEvent(final Event event) {
        eventDispatcher.dispatch(event);
    }

    public List<Booking> getBookings() {
        return Collections.unmodifiableList(bookings);
    }
}