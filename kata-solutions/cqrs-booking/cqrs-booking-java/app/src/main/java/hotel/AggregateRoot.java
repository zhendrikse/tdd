import java.util.List;
import java.util.UUID;

public interface AggregateRoot {
   void apply(final Event event);
   UUID getId();
}