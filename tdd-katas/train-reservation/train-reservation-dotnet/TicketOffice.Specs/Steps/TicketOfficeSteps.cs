using TicketOffice;
using FluentAssertions;
using TechTalk.SpecFlow;

namespace TicketOffice.Specs.Steps;

[Binding]
public class TrainReservatonSteps
{
    private readonly TicketOffice _ticketOffice = new TicketOffice();
    private string _booking_reference = "";
    private readonly string _trainId = "express_2000";

    [Given(@"I have made a reservation with booking reference (.*)")]
    public void GivenIHaveMadeAReservationWithBookingReference(string booking_reference)
    {
        var train = RestCalls.MakeTrainSeatsReservationRestCall(_trainId, booking_reference);
        train.seats["1A"].booking_reference.Should().Be(booking_reference);
        train.seats["1B"].booking_reference.Should().Be(booking_reference);
        _booking_reference = booking_reference;
    }

    [When(@"I cancel my reservation")]
    public void WhenICancelMyReservation()
    {
        _ticketOffice.CancelReservation(_trainId, _booking_reference);
    }

    [Then(@"the reservation should be cancelled")]
    public void ThenTheReservedSeatsShouldBeAvailableAgain()
    {
        var train = RestCalls.GetTrainSeatInformation(_trainId);
        train.seats["1A"].booking_reference.Should().Be("");
        train.seats["1B"].booking_reference.Should().Be("");
    }
}
