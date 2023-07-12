package command;

import java.util.UUID;
import java.time.LocalDate;

public class BookingCommand {
    public final UUID clientId; 
    public final String roomName;
    public final LocalDate arrivalDate;
    public final LocalDate departureDate;
    
    public BookingCommand(final UUID clientId, final String roomName, final LocalDate arrivalDate, final LocalDate departureDate) {
        this.clientId = clientId;
        this.roomName = roomName;
        this.arrivalDate = arrivalDate;
        this.departureDate = departureDate;
    }

    @Override
    public String toString() { 
      return "clientId: '" + this.clientId + "', roomName: '" + this.roomName + "', arrivalDate: '" + this.arrivalDate + "', departureDate: '" + this.departureDate + "'";
    } 
}
