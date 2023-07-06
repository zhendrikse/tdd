import java.util.UUID;
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;

public class StubEventSourceRepository implements EventSourceRepository {
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
      this.eventList.stream().forEach(event -> hotel.apply(event));
      return hotel;
  }
  
  @Override
  public void save(final UUID aggregateRootId, final Event newEvent) {
      this.eventList.add(newEvent);
  }

  public List<Event> getEventsFor(final UUID aggregateRootId) {
      return Collections.unmodifiableList(this.eventList);
  }
}