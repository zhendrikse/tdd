import java.util.UUID;

public interface EventSourceRepository {
  void save(UUID aggregateRootId, Event event);
  void load(AggregateRoot aggregateRoot);
}