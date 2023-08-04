using Kata;
using System;

namespace Kata.UnitTests;

public class FreeDrinksVendingMachine : IDisposable
{
    private VendingMachine vendingMachine;
    private Choice _choice; 

    // https://xunit.net/docs/shared-context
    public FreeDrinksVendingMachine()
    {
        vendingMachine = new VendingMachine();
        vendingMachine.Configure(Choice.FIZZY_ORANGE, Can.FANTA);
        vendingMachine.Configure(Choice.COLA, Can.COKE);
    }

    public void Dispose()
    {
        // vendingMachine = (VendingMachine) null;
    }

    [Fact]
    void VendingMachineDeliversNothingWhenChoiceIsMade()
    {
        Given(Choice.WATER);
        Expect(Can.NOTHING);
    }
  
    [Fact]
    void VendingMachineDeliversCokeWhenColaChoiceIsMade()
    {
        Given(Choice.COLA);
        Expect(Can.COKE);
    }

    [Fact]
    void VendingMachineDeliversFantaWhenFizzyOrangeChoiceIsMade()
    {
        Given(Choice.FIZZY_ORANGE);
        Expect(Can.FANTA);
    }

    private void Given(Choice choice)
    {
        _choice = choice;
    }

    private void Expect(Can can) 
    {
        Assert.Equivalent(can, vendingMachine.Deliver(_choice));
    }
}
