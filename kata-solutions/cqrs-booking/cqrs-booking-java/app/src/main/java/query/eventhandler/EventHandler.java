package query.eventhandler;

import event.Event;

public interface EventHandler {
    void onEvent(final Event event);
}