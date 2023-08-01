package hotel;

import java.util.UUID;
import java.time.LocalDate;

/**
 * Value object, hence may be used through the application, i.e. both
 * on the command and query sides.
 */
public class Booking {
    public final UUID clientId;
    public final Room room;
    public final LocalDate arrivalDate;
    public final LocalDate departureDate;

    public Booking(final UUID clientId, final Room room, final LocalDate arrivalDate, final LocalDate departureDate) {
        this.clientId = clientId;
        this.room = room;
        this.arrivalDate = arrivalDate;
        this.departureDate = departureDate;
    }

    public boolean doesConflictWith(final Booking anotherBooking) {
        return anotherBooking.room.equals(room) &&
                !(anotherBooking.arrivalDate.isAfter(departureDate) ||
                        anotherBooking.departureDate.isBefore(arrivalDate));
    }
}