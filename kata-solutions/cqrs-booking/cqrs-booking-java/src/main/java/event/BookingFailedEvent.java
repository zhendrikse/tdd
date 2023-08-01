package event;

import java.util.UUID;
import java.time.LocalDate;

import hotel.Room;

public class BookingFailedEvent implements Event {
  public final UUID clientId;
  public final Room room;
  public final LocalDate arrivalDate;
  public final LocalDate departureDate;

  public BookingFailedEvent(final UUID clientId, final Room room, final LocalDate arrivalDate,
      final LocalDate departureDate) {
    this.clientId = clientId;
    this.room = room;
    this.arrivalDate = arrivalDate;
    this.departureDate = departureDate;
  }

  @Override
  public String toString() {
    return "clientId: '" + this.clientId + "', room: '" + this.room + "', arrivalDate: '" + this.arrivalDate
        + "', departureDate: '" + this.departureDate + "'";
  }
}