using System;
using System.ComponentModel;

namespace Kata;

public enum Can : ushort
{
    [Description("No can")] NOTHING,
    [Description("Can of Coke")] COKE
}

public enum Choice : ushort
{
    [Description("Cola choice")] COLA
}

public class VendingMachine
{
    private Can canOfChoice = Can.NOTHING;
  
    public void Configure(Choice choice, Can can) 
    {
        this.canOfChoice = can;
    }
  
    public Can Deliver(Choice choice)
    {
        return this.canOfChoice;
    }
}
