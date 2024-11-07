
using System.Data;
using System.Globalization;
using System.Runtime.CompilerServices;
using System.Security.Cryptography;

namespace Kata;

public class LcdDigits
{
    private static string _digits = 
    " _     _  _     _  _  _  _  _ " +  
    "| |  | _| _||_||_ |_   ||_||_|" +  
    "|_|  ||_  _|  | _||_|  ||_| _|";

    private static string[] ConvertToSingleDigitStringArray(int number) {
        return (from i in Enumerable.Range(0, 3) select _digits.Substring(i * 30 + number * 3, 3)).ToArray();
    }

    private static string[] AddDigits(string[] digit_1, string[] digit_2) {
         return (from i in Enumerable.Range(0, 3) select digit_1[i] + digit_2[i]).ToArray();
    }

    public static string[] NumberAsString(int number)
    {
        int size = ("" + number).Length;
        int power = 1;
        for (int i = 1; i < size; i++)
            power *= 10;

        if (power == 1)
            return ConvertToSingleDigitStringArray(number);
        else 
            return AddDigits(ConvertToSingleDigitStringArray(number / power), NumberAsString(number % power));
    }

    public static string GetDigits(int number) {
        string[] numberAsString = NumberAsString(number);
        return numberAsString[0] + "\r\n" + numberAsString[1] + "\r\n" + numberAsString[2] + "\r\n";
    }
}
