using TicketOffice;
using FluentAssertions;
using TechTalk.SpecFlow;

namespace TicketOffice.Specs.Steps;

[Binding]
public class TrainReservatonSteps
{
    private readonly TicketOffice _calculator = new TicketOffice();
    private int _result;

    [Given(@"I have entered (.*) into the calculator")]
    public void GivenIHaveEnteredIntoTheCalculator(int number)
    {
        _calculator.FirstNumber = number;
    }

    [Given(@"I have also entered (.*) into the calculator")]
    public void GivenIHaveAlsoEnteredIntoTheCalculator(int number)
    {
        _calculator.SecondNumber = number;
    }

    [When(@"I press add")]
    public void WhenIPressAdd()
    {
        _result = _calculator.Add();
    }

    [Then(@"the result should be (.*) on the screen")]
    public void ThenTheResultShouldBeOnTheScreen(int expectedResult)
    {
        _result.Should().Be(expectedResult);
    }
}
