using System;
using System.Text.RegularExpressions;

namespace TicketOffice;

public class TicketOffice
{
    public int FirstNumber { set; private get; }
    public int SecondNumber { set; private get; }

    public int Add()
    {
        return FirstNumber + SecondNumber;
    }
}
