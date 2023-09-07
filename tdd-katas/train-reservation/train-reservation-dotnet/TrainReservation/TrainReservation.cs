using System;
using System.Text.RegularExpressions;

namespace TrainReservation;

public class TrainReservation
{
    public int FirstNumber { set; private get; }
    public int SecondNumber { set; private get; }

    public int Add()
    {
        return FirstNumber + SecondNumber;
    }
}
