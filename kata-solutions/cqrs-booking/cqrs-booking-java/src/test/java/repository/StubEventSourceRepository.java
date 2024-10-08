package repository;

import java.util.UUID;
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;
import java.util.stream.Stream;

import event.Event;
import hotel.Hotel;

public class StubEventSourceRepository implements EventSourceRepository<Hotel> {
  private final List<Event> eventList;

  public StubEventSourceRepository() {
    this(new ArrayList<Event>());
  }

  public StubEventSourceRepository(final List<Event> events) {
    this.eventList = events;
  }

  @Override
  public Hotel load(final UUID aggregateRootId) {
    Hotel hotel = new Hotel(this);
    this.eventList.stream().forEach(hotel::onEvent);
    return hotel;
  }

  @Override
  public void save(final UUID aggregateRootId, final Event newEvent) {
    this.eventList.add(newEvent);
  }

  public List<Event> getEventsFor(final UUID aggregateRootId) {
    return Collections.unmodifiableList(this.eventList);
  }

  @Override
  public Stream<Event> loadStream(final UUID aggregateRootId) {
    return null;
  }
}