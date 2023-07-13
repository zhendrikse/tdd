package query.eventhandler;

import java.util.List;
import java.util.ArrayList;
import java.util.Collections;
import java.util.function.Consumer;
import java.util.Map;
import java.util.HashMap;

import event.BookingCreatedEvent;
import event.Event;
import event.EventHandler;
import event.EventDispatcher;

import hotel.Booking;

import event.EventDispatcher;
import event.BookingCreatedEvent;
import event.BookingFailedEvent;

public class BookingEventHandler implements EventHandler {
    private final List<Booking> bookings = new ArrayList<>();
    private final EventDispatcher eventDispatcher = new EventDispatcher(this);

    @Override
    public void onEvent(final BookingCreatedEvent event) {
        BookingCreatedEvent bookingEvent = (BookingCreatedEvent) event;
        bookings.add(new Booking(bookingEvent.clientId, bookingEvent.room, bookingEvent.arrivalDate, bookingEvent.departureDate));
    }

    @Override 
    public void onEvent(final BookingFailedEvent event) {}

    @Override
    public void onEvent(final Event event) {
        eventDispatcher.dispatch(event);
    }

    public List<Booking> getBookings() {
        return Collections.unmodifiableList(bookings);
    }
}