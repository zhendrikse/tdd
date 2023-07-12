package hotel;

import java.util.List;
import java.util.UUID;

import event.Event;
import event.EventHandler;

public interface AggregateRoot extends EventHandler {
   UUID getId();
}