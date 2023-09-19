using Xunit;
using System;

namespace TicketOffice.Tests;

public class TicketOfficeTest
{
    private string _booking_reference;

    public TicketOfficeTest() 
    {
        _booking_reference = "";
    }


    [Fact]
    public void SampleSeatReservation()
    {
        var confirmation = "{\"train_id\": \"express_2000\", \"booking_reference\": \"75bcd15\", \"seats\": [\"1A\", \"1B\"]}";
        Assert.Equivalent(confirmation, new TicketOffice().ReserveSeats("express_2000", 2));
    }
}
