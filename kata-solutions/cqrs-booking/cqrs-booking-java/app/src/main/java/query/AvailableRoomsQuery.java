package query;

import java.time.LocalDate;
import java.util.UUID;

public class AvailableRoomsQuery {
  public final LocalDate arrivalDate;
  public final LocalDate departureDate;
  public final UUID hotelId;
  
  public AvailableRoomsQuery(final UUID hotelId, final LocalDate arrivalDate, final LocalDate departureDate) {
    this.arrivalDate = arrivalDate;
    this.departureDate = departureDate;
    this.hotelId = hotelId;
  }
}