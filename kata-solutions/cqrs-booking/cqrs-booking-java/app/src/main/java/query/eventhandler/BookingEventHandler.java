package query.eventhandler;

import java.util.List;
import java.util.ArrayList;
import java.util.Collections;

import event.BookingCreatedEvent;
import event.Event;

import hotel.Booking;

public class BookingEventHandler implements EventHandler {
    private final List<Booking> bookings = new ArrayList<>();

    @Override
    public void onEvent(final Event event) {
        if (event instanceof BookingCreatedEvent) {
            BookingCreatedEvent bookingEvent = (BookingCreatedEvent) event;
            bookings.add(new Booking(bookingEvent.clientId, bookingEvent.roomName, bookingEvent.arrivalDate, bookingEvent.departureDate));
        }
    }

    public List<Booking> getBookings() {
        return Collections.unmodifiableList(bookings);
    }
}