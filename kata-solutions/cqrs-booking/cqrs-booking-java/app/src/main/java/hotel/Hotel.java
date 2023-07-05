import java.util.List;
import java.util.ArrayList;
import java.util.UUID;
import java.util.Collections;
import java.time.LocalDate;

public class Hotel implements AggregateRoot {
  private final List<Booking> bookings = new ArrayList<>();
  private final List<Event> changes;

  public Hotel(final List<Event> events) {
    for (final Event event : events)
      apply(event);
    this.changes = new ArrayList<Event>();
  }

  private boolean canBookingBeMade(final Booking requestedBooking, final Booking existingBooking) {
      if (!existingBooking.roomName.equals(requestedBooking.roomName)) 
          return true;

      if (existingBooking.isDateBetweenArrivalAndDepartureDates(requestedBooking.arrivalDate))
          return false;
  
      return true;
  }

  private boolean canBookingBeMade(final Booking requestedBooking) {
    for (final Booking existingBooking : this.bookings) {
      if (!canBookingBeMade(requestedBooking, existingBooking))
        return false;
    }
    
    return true;
  }
  
  public void onCommand(final BookingCommand command) {
      final Booking requestedBooking = new Booking(
        command.clientId, command.roomName, command.arrivalDate, command.departureDate);
      if (canBookingBeMade(requestedBooking))
        bookingSucceeds(command);
      else
        bookingFails(command);
  }

  private void bookingFails(final BookingCommand command) {
      BookingFailedEvent event = new BookingFailedEvent(
        command.clientId, command.roomName, command.arrivalDate, 
command.departureDate);
      this.changes.add(event);
  }

  private void bookingSucceeds(final BookingCommand command) {
      BookingCreatedEvent event = new BookingCreatedEvent(
        command.clientId, command.roomName, command.arrivalDate, command.departureDate);
      this.changes.add(event);
      onEvent(event);
  }
    
  private void onEvent(final BookingCreatedEvent event) {
      this.bookings.add(new Booking(
        event.clientId, event.roomName, event.arrivalDate, event.departureDate));
  }

  private void apply(final Event event) {
    if (event instanceof BookingCreatedEvent) 
      onEvent((BookingCreatedEvent) event);
  }

  @Override
  public List<Event> persist() {
    return Collections.unmodifiableList(this.changes);
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

      public boolean isDateBetweenArrivalAndDepartureDates(final LocalDate aDate) {
          return aDate.compareTo(this.arrivalDate) >= 0 && aDate.compareTo(this.departureDate) <=0;
      }
  }
}