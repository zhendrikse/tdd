import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.BeforeEach;
import java.util.UUID;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Stream;
import java.time.LocalDate;

class InMemoryEventSourceRepositoryTest {
    private static final String BLUE_ROOM_NAME = "The Blue Room";
    private static final String RED_ROOM_NAME = "The Red Room";
    private static final LocalDate AN_ARRIVAL_DATE = LocalDate.of(2020, 1, 20);
    private static final LocalDate A_DEPARTURE_DATE = LocalDate.of(2020, 1, 22);
    private static final UUID A_CLIENT_UUID = UUID.randomUUID();

    private final BookingCommand blueRoomBookingCommand = new BookingCommand(
        A_CLIENT_UUID, BLUE_ROOM_NAME, AN_ARRIVAL_DATE, A_DEPARTURE_DATE
      );
  
    private final BookingCommand redRoomBookingCommand = new BookingCommand(
        A_CLIENT_UUID, RED_ROOM_NAME, AN_ARRIVAL_DATE, A_DEPARTURE_DATE
      );

    @Test
    void repositoryContainsBookingCreatedEventAfterSuccessfulBookings() {
        EventSourceRepository repository = new InMemoryEventSourceRepository();
        Hotel hotel = new Hotel(repository);
        hotel.onCommand(blueRoomBookingCommand);
        hotel.onCommand(redRoomBookingCommand);
        
        Stream eventStream = repository.loadStream(hotel.getId());
        assertEquals(eventStream.count(), 2);
    }

    @Test
    void repositoryDistinguishesBetweenDifferentAggregateRoots() {
        EventSourceRepository repository = new InMemoryEventSourceRepository();
        
        Hotel hotel1 = new Hotel(repository);
        hotel1.onCommand(blueRoomBookingCommand);
        Hotel hotel2 = new Hotel(repository);
        hotel2.onCommand(redRoomBookingCommand);
        
        Stream eventStream = repository.loadStream(hotel1.getId());
        assertEquals(eventStream.count(), 1);
    }
}