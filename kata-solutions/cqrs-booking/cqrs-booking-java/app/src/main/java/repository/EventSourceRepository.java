import java.util.UUID;

public interface EventSourceRepository<Hotel> {
  void save(UUID aggregateRootId, Event event);
  Hotel load(UUID aggregateRootId);
}