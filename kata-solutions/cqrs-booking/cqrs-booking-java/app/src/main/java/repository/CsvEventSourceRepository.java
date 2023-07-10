import java.util.UUID;
import java.util.stream.Stream;

public class CsvEventSourceRepository implements EventSourceRepository<Hotel> {
  @Override
  public void save(final UUID aggregateRootId, final Event newEvent) {
    
  }
  
  @Override
  public Hotel load(final UUID aggregateRootId) {
    return null;
  }

  @Override
  public Stream<Event> loadStream(final UUID aggregateRootId) {
    return null;
  }
}