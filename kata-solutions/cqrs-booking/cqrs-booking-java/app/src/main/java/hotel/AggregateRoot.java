package hotel;

import java.util.UUID;

import event.EventHandler;

public interface AggregateRoot extends EventHandler {
   UUID getId();
}