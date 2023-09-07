using Xunit;
using System;

namespace TrainReservation.Tests;

public class TrainReservationTest
{
    private string _result;

    public TrainReservationTest() 
    {
        _result = "";
    }

    [Fact]
    public void EmptyExpressionResultsInSame()
    {
        Given("");
        Expect("");
    }

    [Fact]
    public void NullExpressionProducesEmtpyResult()
    {
        Given(null);
        Expect("");
    }

    [Fact]
    public void JustANumberResultsInTheSame()
    {
        Given("42");
        Expect("42");
    }

    [Fact]
    public void HandlesASingleBinaryOperator()
    {
        Given("4 + 2");
        Expect("4 2 +");        
    }

    [Fact]
    public void HandlesMultipleOperatorsOfSamePrecedence()
    {
        Given("a - 5 + 3");
        Expect("a 5 - 3 +");        
    }

    private void Given(string expression) 
    {
        var algorithm = new TrainReservation();
        _result = algorithm.Transform(expression);
    }

    private void Expect(string expression) 
    {
        Assert.Equivalent(expression, _result);        
    }
}
