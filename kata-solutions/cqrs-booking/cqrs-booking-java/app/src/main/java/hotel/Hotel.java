package hotel;

import static java.util.stream.Collectors.toList;

import java.util.ArrayList;
import java.util.List;
import java.util.UUID;

import command.BookingCommand;
import event.BookingCreatedEvent;
import event.BookingFailedEvent;
import event.Event;
import event.EventDispatcher;
import repository.EventSourceRepository;

public class Hotel implements AggregateRoot {
  private final UUID id = UUID.randomUUID();
  private final EventSourceRepository<Hotel> eventSourceRepository;
  private final List<Booking> bookings = new ArrayList<>();
  private final EventDispatcher eventDispatcher = new EventDispatcher(this);

  public Hotel(final EventSourceRepository<Hotel> repository) {
    this.eventSourceRepository = repository;
  }

  @Override
  public UUID getId() {
    return id;
  }

  private void bookingFails(final BookingCommand command) {
    BookingFailedEvent event = new BookingFailedEvent(command.clientId, command.room, command.arrivalDate,
        command.departureDate);
    onEvent(event);
    this.eventSourceRepository.save(this.id, event);
  }

  private void bookingSucceeds(final BookingCommand command) {
    BookingCreatedEvent event = new BookingCreatedEvent(
        command.clientId, command.room, command.arrivalDate, command.departureDate);
    onEvent(event);
    this.eventSourceRepository.save(this.id, event);
  }

  @Override
  public void onEvent(final BookingFailedEvent event) {
  }

  @Override
  public void onEvent(final BookingCreatedEvent event) {
    this.bookings.add(new Booking(
        event.clientId, event.room, event.arrivalDate, event.departureDate));
  }

  private boolean bookingCanBeMade(final Booking requestedBooking) {
    return this.bookings
        .stream()
        .filter(requestedBooking::doesConflictWith)
        .collect(toList())
        .isEmpty();
  }

  public void onCommand(final BookingCommand command) {
    final Booking requestedBooking = new Booking(
        command.clientId, command.room, command.arrivalDate, command.departureDate);
    if (bookingCanBeMade(requestedBooking))
      bookingSucceeds(command);
    else
      bookingFails(command);
  }

  @Override
  public void onEvent(final Event event) {
    eventDispatcher.dispatch(event);
  }

}
