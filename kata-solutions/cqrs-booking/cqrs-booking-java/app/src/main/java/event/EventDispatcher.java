package event;

import java.util.function.Consumer;
import java.util.Map;
import java.util.HashMap;

public class EventDispatcher {
    private final Map<Class, Consumer<Event>> onEventDispatcher = new HashMap<>();
    private final EventHandler eventHandler;

    public EventDispatcher(final EventHandler eventHandler) {
        initOnEventDispatcherMap();
        this.eventHandler = eventHandler;
    }

    private void initOnEventDispatcherMap() {
        onEventDispatcher.put(BookingCreatedEvent.class, event -> eventHandler.onEvent((BookingCreatedEvent) event));
        onEventDispatcher.put(BookingFailedEvent.class, event -> eventHandler.onEvent((BookingFailedEvent) event));
    }

    public void dispatch(final Event event) {
        onEventDispatcher.get(event.getClass()).accept(event);
    }
}