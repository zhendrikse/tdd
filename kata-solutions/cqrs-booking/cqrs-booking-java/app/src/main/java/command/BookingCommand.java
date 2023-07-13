package command;

import java.util.UUID;
import java.time.LocalDate;
import hotel.Room;

public class BookingCommand {
    public final UUID clientId; 
    public final Room room;
    public final LocalDate arrivalDate;
    public final LocalDate departureDate;
    
    public BookingCommand(final UUID clientId, final Room room, final LocalDate arrivalDate, final LocalDate departureDate) {
        this.clientId = clientId;
        this.room = room;
        this.arrivalDate = arrivalDate;
        this.departureDate = departureDate;
    }

    @Override
    public String toString() { 
      return "clientId: '" + clientId + "', roomName: '" + room + "', arrivalDate: '" + arrivalDate + "', departureDate: '" + departureDate + "'";
    } 
}
