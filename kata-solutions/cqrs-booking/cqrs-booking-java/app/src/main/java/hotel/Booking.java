package hotel;

import java.util.UUID;
import java.time.LocalDate;

/**
 * Value object, hence may be used through the application, i.e. both
 * on the command and query sides.
 */
public class Booking {
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