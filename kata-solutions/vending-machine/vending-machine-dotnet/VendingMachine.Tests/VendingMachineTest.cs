using Kata;
using System;

namespace Kata.UnitTests;

public class FreeDrinksVendingMachine : IDisposable
{
    private VendingMachine vendingMachine;

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
    public void VendingMachineDeliversNothingWhenChoiceIsMade()
    {
        Assert.Equal(Can.NOTHING, vendingMachine.Deliver(Choice.WATER));
    }
  
    [Fact]
    public void VendingMachineDeliversCokeWhenColaChoiceIsMade()
    {
        Assert.Equal(Can.COKE, vendingMachine.Deliver(Choice.COLA));
    }

    [Fact]
    public void VendingMachineDeliversFantaWhenFizzyOrangeChoiceIsMade()
    {
        Assert.Equal(Can.FANTA, vendingMachine.Deliver(Choice.FIZZY_ORANGE));
    }
}
