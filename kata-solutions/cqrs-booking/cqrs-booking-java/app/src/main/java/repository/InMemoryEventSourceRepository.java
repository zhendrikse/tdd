package repository;

import java.util.UUID;
import java.util.stream.Stream;

import java.util.Map;
import java.util.HashMap;
import java.util.List;
import java.util.ArrayList;

import event.Event;
import hotel.Hotel;

public class InMemoryEventSourceRepository implements EventSourceRepository<Hotel> {
  private final Map<UUID, List<Event>> eventStore = new HashMap<>();

  @Override
  public void save(final UUID aggregateRootId, final Event newEvent) {
      if (!eventStore.containsKey(aggregateRootId))
        eventStore.put(aggregateRootId, new ArrayList<>());

      this.eventStore.get(aggregateRootId).add(newEvent);
  }
  
  @Override
  public Hotel load(final UUID aggregateRootId) {
    return null;
  }

  @Override
  public Stream<Event> loadStream(final UUID aggregateRootId) {
    return eventStore.get(aggregateRootId).stream();
  }
}