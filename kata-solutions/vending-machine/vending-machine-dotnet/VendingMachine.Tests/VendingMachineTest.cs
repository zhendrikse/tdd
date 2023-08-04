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
    }

    public void Dispose()
    {
        // vendingMachine = (VendingMachine) null;
    }

    [Fact]
    public void VendingMachineDeliversNothingWhenChoiceIsMade()
    {
        Assert.Equal(Can.NOTHING, vendingMachine.Deliver(Choice.COLA));
    }
  
    [Fact]
    public void VendingMachineDeliversCokeWhenColaChoiceIsMade()
    {
        vendingMachine.Configure(Choice.COLA, Can.COKE);
        Assert.Equal(Can.COKE, vendingMachine.Deliver(Choice.COLA));
    }
}