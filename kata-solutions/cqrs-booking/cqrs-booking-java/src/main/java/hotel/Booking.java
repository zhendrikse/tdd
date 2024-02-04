package hotel;

import java.util.UUID;
import java.time.LocalDate;

/**
 * Value object, hence may be used through the application, i.e. both
 * on the command and query sides.
 */
public record Booking(UUID clientId, Room room, LocalDate arrivalDate, LocalDate departureDate) {

    public boolean doesConflictWith(final Booking anotherBooking) {
        return anotherBooking.room.equals(room) &&
                !(anotherBooking.arrivalDate.isAfter(departureDate) ||
                        anotherBooking.departureDate.isBefore(arrivalDate));
    }
}