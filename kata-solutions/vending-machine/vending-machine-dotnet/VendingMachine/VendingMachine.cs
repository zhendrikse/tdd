using System;
using System.ComponentModel;

namespace Kata;

public enum Can : ushort
{
    [Description("No can")] NOTHING,
    [Description("Can of Fanta")] FANTA,
    [Description("Can of Coke")] COKE
}

public enum Choice : ushort
{
    [Description("Cola choice")] COLA,
    [Description("Fizzy orange choice")] FIZZY_ORANGE,
    [Description("Water choice")] WATER
}

public class VendingMachine
{
    private Can canOfChoice = Can.NOTHING;
    private Dictionary<Choice, Can> choiceCanMap = new Dictionary<Choice, Can>();

    public void Configure(Choice choice, Can can) 
    {
        canOfChoice = can;
        choiceCanMap[choice] = can;
    }
  
    public Can Deliver(Choice choice)
    {
        if (!choiceCanMap.ContainsKey(choice))
            return Can.NOTHING;
        
        return choiceCanMap[choice];
    }
}
