package repository;

import java.util.UUID;
import java.util.stream.Stream;

import event.Event;

public interface EventSourceRepository<Hotel> {
  void save(UUID aggregateRootId, Event newEvent);

  Hotel load(UUID aggregateRootId);

  Stream<Event> loadStream(UUID aggregateRootId);
}