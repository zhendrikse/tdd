using Xunit;
using System;

namespace TrainReservation.Tests;

public class TrainReservationTest
{
    private int _result;

    public TrainReservationTest() 
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
        var calculator = new TrainReservation();
        calculator.FirstNumber = a;
        calculator.SecondNumber = b;
        _result = calculator.Add();
    }

    private void Expect(int addition) 
    {
        Assert.Equivalent(addition, _result);        
    }
}
