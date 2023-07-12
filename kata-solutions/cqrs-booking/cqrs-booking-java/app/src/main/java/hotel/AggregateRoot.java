package hotel;

import java.util.List;
import java.util.UUID;

import event.Event;

public interface AggregateRoot {
   void apply(final Event event);
   UUID getId();
}