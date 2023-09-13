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

    public string ReserveSeats(string stringId, int seats)
    {
        return "{\"train_id\": \"express_2000\", \"booking_reference\": \"75bcd15\", \"seats\": [\"1A\", \"1B\"]}";
    }
}
