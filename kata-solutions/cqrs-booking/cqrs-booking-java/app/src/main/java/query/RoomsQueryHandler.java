package query;

import java.time.LocalDate;
import java.util.List;
import java.util.ArrayList;
import java.util.UUID;
import java.util.stream.Stream;
import static java.util.stream.Collectors.toList;

import event.Event;
import repository.EventSourceRepository;
import hotel.Room;
import hotel.Booking;
import query.eventhandler.BookingEventHandler;

public class RoomsQueryHandler {
  private final EventSourceRepository eventRepository;
  private List<Booking> allBookings = new ArrayList<>();

  public RoomsQueryHandler(final EventSourceRepository eventRepository) {
    this.eventRepository = eventRepository;
  }

  private void updateListWithAllBookings(final UUID hotelId) {
    final BookingEventHandler bookingEventHandler = new BookingEventHandler();            
    final Stream<Event> eventStream = eventRepository.loadStream(hotelId);
    eventStream.forEach(bookingEventHandler::onEvent);
    allBookings = bookingEventHandler.getBookings();    
  }

  private boolean roomAvailable(final Booking queryBooking) {
      return allBookings
        .stream()
        .filter(queryBooking::doesConflictWith)
        .map(booking -> booking.room)
        .collect(toList())
        .isEmpty();
  }

  private List<Room> filterAvailableRoomsFromAllRooms(final AvailableRoomsQuery query) {
    updateListWithAllBookings(query.hotelId);
    return Stream
      .of(Room.values())
      .filter(room -> roomAvailable(
        new Booking(UUID.randomUUID(), room, query.arrivalDate, query.departureDate)))
      .collect(toList());
  }

  public List<Room> onQuery(final AvailableRoomsQuery query) {
    return filterAvailableRoomsFromAllRooms(query);
  }
}