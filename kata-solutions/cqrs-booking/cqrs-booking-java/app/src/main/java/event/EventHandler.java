package event;

import event.Event;

public interface EventHandler {
    void onEvent(BookingFailedEvent event);

    void onEvent(BookingCreatedEvent event);

    void onEvent(Event event);
}