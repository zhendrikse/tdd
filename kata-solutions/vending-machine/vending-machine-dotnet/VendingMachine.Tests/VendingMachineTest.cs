using Xunit;
using Kata;
using System;

namespace Kata.UnitTests;

public class FreeDrinksVendingMachine : IDisposable
{
    private VendingMachine vendingMachine;

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
        // var vendingMachine = new VendingMachine();
        Assert.Equal(Can.NOTHING, vendingMachine.Deliver(Choice.COLA));
    }
  
    [Fact]
    public void VendingMachineDeliversCokeWhenColaChoiceIsMade()
    {
        // var vendingMachine = new VendingMachine();
        vendingMachine.Configure(Choice.COLA, Can.COKE);
        Assert.Equal(Can.COKE, vendingMachine.Deliver(Choice.COLA));
    }
}
