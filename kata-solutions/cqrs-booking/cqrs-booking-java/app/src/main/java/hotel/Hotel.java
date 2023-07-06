import java.util.UUID;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.HashMap;
import java.util.function.Consumer;
import java.time.LocalDate;
import static java.util.stream.Collectors.toList;

public class Hotel implements AggregateRoot {
    private final UUID id = UUID.randomUUID();
    private final EventSourceRepository eventSourceRepository;
    private final List<Booking> bookings = new ArrayList<>();
    private final Map<Class, Consumer<Event>> onEventDispatcher = new HashMap<>();

    public Hotel(final EventSourceRepository repository) {
        this.eventSourceRepository = repository;
        this.onEventDispatcher.put(BookingCreatedEvent.class, event -> onEvent((BookingCreatedEvent) event));
        this.onEventDispatcher.put(BookingFailedEvent.class, event -> onEvent((BookingFailedEvent) event));
    }

    @Override 
    public UUID getId() {
        return id;
   }

   private void bookingFails(final BookingCommand command) {
        BookingFailedEvent event = new BookingFailedEvent(
          command.clientId, command.roomName, command.arrivalDate, 
  command.departureDate);
        onEvent(event);
        this.eventSourceRepository.save(this.id, event);
    }
  
    private void bookingSucceeds(final BookingCommand command) {
        BookingCreatedEvent event = new BookingCreatedEvent(
          command.clientId, command.roomName, command.arrivalDate, command.departureDate);
        onEvent(event);
        this.eventSourceRepository.save(this.id, event);
    }    
      
    private void onEvent(final BookingFailedEvent event) {}
      
    private void onEvent(final BookingCreatedEvent event) {
        this.bookings.add(new Booking(
          event.clientId, event.roomName, event.arrivalDate, event.departureDate));
    }

  private boolean bookingCanBeMade(final Booking requestedBooking) {
    return this.bookings
      .stream()
      .filter(booking -> booking.doesConflictWith(requestedBooking))
      .collect(toList())
      .isEmpty();
  }
  
  public void onCommand(final BookingCommand command) {
      final Booking requestedBooking = new Booking(
        command.clientId, command.roomName, command.arrivalDate, command.departureDate);
      if (bookingCanBeMade(requestedBooking))
        bookingSucceeds(command);
      else
        bookingFails(command);
  }
  
  @Override
  public void apply(final Event event) {
    this.onEventDispatcher.get(event.getClass()).accept(event);
  }

  class Booking implements Event {
      public final UUID clientId; 
      public final String roomName;
      public final LocalDate arrivalDate;
      public final LocalDate departureDate;
      
      public Booking(final UUID clientId, final String roomName, final LocalDate arrivalDate, final LocalDate departureDate) {
          this.clientId = clientId;
          this.roomName = roomName;
          this.arrivalDate = arrivalDate;
          this.departureDate = departureDate;
      }

      public boolean doesConflictWith(final Booking anotherBooking) {
          return anotherBooking.roomName.equals(this.roomName) && 
            !(anotherBooking.arrivalDate.isAfter(this.departureDate) ||
            anotherBooking.departureDate.isBefore(this.arrivalDate));
      }
  }
}
