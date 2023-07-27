package repository;

import java.util.UUID;
import java.util.stream.Stream;

import event.Event;
import hotel.AggregateRoot;

public interface EventSourceRepository<T extends AggregateRoot> {
  void save(UUID aggregateRootId, Event newEvent);

  T load(UUID aggregateRootId);

  Stream<Event> loadStream(UUID aggregateRootId);
}