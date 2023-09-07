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
    public void EmptyExpressionResultsInSame()
    {
        Given(5, 3);
        Expect(8);
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
