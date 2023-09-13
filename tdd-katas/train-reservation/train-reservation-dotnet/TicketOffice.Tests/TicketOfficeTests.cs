using Xunit;
using System;

namespace TicketOffice.Tests;

public class TicketOfficeTest
{
    private int _result;

    public TicketOfficeTest() 
    {
        _result = 0;
    }

    [Fact]
    public void AddTwoNumbers()
    {
        Given(5, 3);
        Expect(8);
    }

    [Fact]
    public void SampleSeatReservation()
    {
        var confirmation = "{\"train_id\": \"express_2000\", \"booking_reference\": \"75bcd15\", \"seats\": [\"1A\", \"1B\"]}";
        Assert.Equivalent(confirmation, new TicketOffice().ReserveSeats("express_2000", 2));
    }

    private void Given(int a, int b) 
    {
        var calculator = new TicketOffice();
        calculator.FirstNumber = a;
        calculator.SecondNumber = b;
        _result = calculator.Add();
    }

    private void Expect(int addition) 
    {
        Assert.Equivalent(addition, _result);        
    }
}
