import java.util.UUID;

public interface EventSourceRepository<Hotel> {
  void save(UUID aggregateRootId, Event newEvent);
  Hotel load(UUID aggregateRootId);
}