using Xunit;
using System;

namespace Kata.Tests;

public class LcdDigitsTest
{
    [Fact]
    public void Digit_the_number_0()
    {
        string expect = " _ " + "\r\n" +
                        "| |" + "\r\n" +
                        "|_|" + "\r\n";

        Assert.Equivalent(expect, LcdDigits.GetDigits(0));
    }

    [Fact]
    public void Digit_the_number_1()
    {
        string expect = "   " + "\r\n" +
                        "  |" + "\r\n" +
                        "  |" + "\r\n";

        Assert.Equivalent(expect, LcdDigits.GetDigits(1));
    }

    [Fact]
    public void Digit_the_number_2()
    {
        string expect = " _ " + "\r\n" +
                        " _|" + "\r\n" +
                        "|_ " + "\r\n";

        Assert.Equivalent(expect, LcdDigits.GetDigits(2));
    }

    [Fact]
    public void Digit_the_number_34()
    {
        string expect = " _    " + "\r\n" +
                        " _||_|" + "\r\n" +
                        " _|  |" + "\r\n";

        Assert.Equivalent(expect, LcdDigits.GetDigits(34));
    }


    [Fact]
    public void Digit_the_number_357()
    {
        string expect = " _  _  _ " + "\r\n" +
                        " _||_   |" + "\r\n" +
                        " _| _|  |" + "\r\n";

        Assert.Equivalent(expect, LcdDigits.GetDigits(357));
    }
}
