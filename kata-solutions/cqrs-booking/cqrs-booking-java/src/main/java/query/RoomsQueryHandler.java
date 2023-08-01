package query;

import static java.util.stream.Collectors.toList;

import java.util.ArrayList;
import java.util.List;
import java.util.UUID;
import java.util.stream.Stream;

import event.Event;
import hotel.Booking;
import hotel.Hotel;
import hotel.Room;
import query.eventhandler.BookingEventHandler;
import repository.EventSourceRepository;

public class RoomsQueryHandler {
  private final EventSourceRepository<Hotel> eventRepository;
  private List<Booking> allBookings = new ArrayList<>();

  public RoomsQueryHandler(final EventSourceRepository<Hotel> eventRepository) {
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