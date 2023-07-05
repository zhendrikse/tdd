import java.util.List;

public interface AggregateRoot {
   List<Event> persist();
}